from pymongo import MongoClient
import pprint
#attaching URL to variable
url = "mongodb+srv://admin:admin@cluster0.wcq8x.mongodb.net/pytech?retryWrites=true&w=majority";

#declaring client with URL and MongoClient
client = MongoClient(url)

#Database established, pytech
db = client.pytech

#calling our collection inside the database
collection = db["students"]


#finding the documents and printing them out
docs = list(collection.find({}))
#for x in docs:
#    print(docs)
print(docs)
#What I just did output the actual list of data instead of the cursor instance in the Python Debug Window.

#finding a document and printing it out
db.collection_names
doc2 = collection.find_one({"student_id":"1007"})
#collection_name does not exist and collection_names is deprecated.
#reference directly to the collection to take effect with find_one() command
print(doc2["student_id"]) # OKAY NOW IT PRINTS OUT THE PROPER ID.