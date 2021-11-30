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



#Display
print("Deletion Display - Filtered to names and IDs.")
student_profiles1 = collection.find({}, {"_id":0, "first_name":1, "last_name":1, "student_id":1} )
for iter in student_profiles1:
    print(iter)
print("\n")

#Insert
collection.insert_one({"first_name":"Roy", "last_name":"Carmack", "student_id":"1010"})


#Display
print("Showing New Profile Addition")
student_profiles2 = collection.find({}, {"_id":0, "first_name":1, "last_name":1, "student_id":1} )
for iter in student_profiles2:
    print(iter)
print("\n")

#Display of the singular profile through find_one method
print("Showing New Profile - Error, unable to get the newest addition")
indie_profile = collection.find_one({},{"_id":1, "first_name":1, "last_name":1, "student_id":"1010"})
print(indie_profile)
print("\n")
#attempting to use the find_one method returned Jane Doe with an ID of 1010. Was working fine earlier.
#IT EVEN RETURNS THE OBJECT ID. I HAVE NO IDEA WHAT IS GOING ON.
#it's clearly adding the new profile to mongoDB, but it's not displaying the correct one.
#Tested the other pytech_update.py script. Jane Doe. Something is wrong with one of the extensions, not the code.
#Pushing this and going to bed.


#Delete
collection.delete_one({"student_id":"1010"})

#Display
print("Showing Default Profiles")
student_profiles3 = collection.find({}, {"_id":0, "first_name":1, "last_name":1, "student_id":1} )
for iter3 in student_profiles3:
    print(iter3)