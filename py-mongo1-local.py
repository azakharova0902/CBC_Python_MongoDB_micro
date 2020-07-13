import pymongo

# Setting a connection

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["PyDB_Local"]
coll = mydb["employees"]

#  Displaying records from "employees" collection
record = coll.find()

for r in record:
    print(r)