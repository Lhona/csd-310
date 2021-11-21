#from pymongo import MongoClient
#url = "mongodb+srv://admin:admin@cluster0.wcq8x.mongodb.net/pytech?retryWrites=true&w=majority";
#client = MongoClient(url)
#db = client.pytech
#print(db.list_collection_names)

import pymongo

myclient = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.wcq8x.mongodb.net/pytech?retryWrites=true&w=majority")

#use database "organisation"
mydb = myclient['pytech']

print("List of collections\n--------------------")
#list the collections
print(mydb.list_collection_names)