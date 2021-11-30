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

#student_calls = db.students.find({}, {"_id": 0, "first_name" : 1, "last_name": 1, "student_id": 1})
#first_name_calls = db.students.find({}, {"_id": 0, "first_name": 1})
#last_name_calls = db.students.find({}, {"_id": 0, "last_name" : 1})
#student_id_calls = db.students.find({}, {"_id": 0, "student_id" : 1})
#spent a good while trying to figure out how to iterate the above three before I decided to just keep it simple.




print("Find Query Display - Filtered to names and IDs.")

student_profiles = collection.find({}, {"_id":0, "first_name":1, "last_name":1, "student_id":1} )
for iter in student_profiles:
    print(iter)

#updates the last name
collection.update_one({"student_id":"1007"}, {"$set":{"last_name":"Montana"}})

#assign the value
updated_profile = collection.find_one({},{"_id":0,"first_name":1, "last_name":1, "student_id":"1007"})

#print the value WITHOUT the Object ID string.
print("\nUpdated Student Profile")
print(updated_profile)

#for repeat tests.
collection.update_one({"student_id":"1007"}, {"$set":{"last_name":"Jones"}})

#to ensure that the script is actually outputting text.
#print("hello world")