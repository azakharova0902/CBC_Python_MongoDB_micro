import pymongo

# Setting a connection

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["PyDB_Local"]
coll = mydb["employees"]


def display_options():
    print("----------")
    print("1. Add a record")
    print("2. View a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")
#display_options() just to display the results up to here
    user_option = input("Enter option number: ")
    return user_option


#  Let's now define our helper function
def get_record():
    print("") 
    name = input("Enter your first name: ")
    last = input("Enter your last name: ")

    try:
        document = coll.find_one({'first_name':name.lower(), 'last_name':last.lower()})
    except:
        print("Ooops..looks like there was an error accessing the database")

    if not document:
        print("")
        print("Sorry! No results have been found for your request.")
   
    return document

#  Let's now write a function that creates new records in our database
def add_record():
    print("")
    name = input("Enter your name: ")
    last = input("Enter your last name: ")
    email = input("Enter your email: ")
    title = input("Enter your job title: ")
    salary = float(input("Enter your salary: "))


    new_record = {
        "first_name" : name.lower(),
        "last_name" : last.lower(),
        "email" : email.lower(),
        "job_title" : title.lower(),
        "salary" : salary
    }

    try:
        coll.insert_one(new_record)
        print("")
        print("Document has been successfylly inserted")
    
    except:
        print("Ooops..looks like there was an error accessing the database")


# Let's now write a function that finds a record in our database
def find_record():
    record = get_record()
    if record:
        print("")
        for key, value in record.items():
            if key != "_id":
                if (isinstance(value,str)):
                    print(key.capitalize(),":" , value.capitalize())
                else:
                    print(key.capitalize(),":", value)


# Let's now write a function that updates a record in our database
def update_record():
    update = get_record()
    if update:
        update_doc = {}
        print("")
        for key, value in update.items():
            if key != "_id":
                update_doc[key] = input(f"{key} [{value}] :").lower()

                if update_doc[key] == "":
                    update_doc[key] = value

        try:
            coll.update_one(update, {'$set': update_doc})
            print("")
            print("Document has been updated")
        except:
            print("ooops..there was an error")


# Let's now write a function that deletes a record from our database
def delete_record():
    delete = get_record()
    if delete:
        print("")
        
        for key, value in delete.items():
            if (isinstance(value,str)):
                print(key.capitalize(), ": ", value.capitalize())
            else:
                print(key.capitalize(), ": ", value)

        print("")
        confirm = input("Would you like to delete this document? \nY or N: ")
        print("")

        if confirm.lower() == "y":
            try:
                coll.delete_one(delete)
                print("")
                print("Document has been deleted.")
            except:
                print("Ooops..looks like there was an error accessing the database")
        else:
            print("Document has not deleted.")

def keep_asking():

    while True:
        print("------------------------")
        select = display_options()
        if select == "1":
            print("You have selected option 1 :)")
            add_record()

        elif select == "2":
            print("You have selected option 2 :)")
            find_record()

        elif select == "3":
            print("You have selected option 3 :)")
            edit_record()

        elif select == "4":
            print("You have selected option 4 :)")
            delete_record()

        elif select == "5":
            myclient.close()
            break
        else:
            print("Sorry, this was not a valid option, please try again")

keep_asking()
