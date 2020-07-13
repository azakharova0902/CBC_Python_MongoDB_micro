import pymongo

# Setting a connection

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["PyDB_Local"]
coll = mydb["employees"]

#  Displaying records from "employees" collection
record = coll.find()

for r in record:
    print(r)

# Inserting a new record into "employees" collection
new_record = {
 "first":"Jane","last":"Snow",
 "email":"js@gmail.com","job_title":"Marketing Manager","hire_date":"05.10.2016",
 "salary": 65000
}

coll.insert_one(new_record)

record = coll.find()
for r in record:
    print(r)

# Inserting multiple new records into "employees" collection
many_records = [
{"first":"Anthony","last":"Walters",
 "email":"aw@gmail.com","job_title":"Manager","hire_date":"11.10.2017",
 "salary": 67000},
 {"first":"Joshua","last":"Andrews",
 "email":"ja@gmail.com","job_title":"HR Manager","hire_date":"12.10.2019",
 "salary": 60000},
 {"first":"Kira","last":"Jefferson",
 "email":"kj@gmail.com","job_title":"UX Designer","hire_date":"09.04.2017",
 "salary": 61000}
 ]

coll.insert_many(many_records)

record = coll.find()
for r in record:
    print(r)