from pymongo import MongoClient
#attaching URL to variable
url = "mongodb+srv://admin:admin@cluster0.wcq8x.mongodb.net/pytech?retryWrites=true&w=majority";

#declaring client with URL and MongoClient
client = MongoClient(url)

#Database established, pytech
db = client.pytech

#calling our collection inside the database
collection = db["students"]

#declaring variables to be inserted with each individual document in the database
student_Fred = {
            "first_name":"Fred",
            "last_name":"Jones",
            "student_id":"1007"
        }
student_Jane = {
            "first_name":"Jane",
            "last_name":"Doe",
            "student_id":"1008"
        }
student_West = {
            "first_name":"West",
            "last_name":"Donovan",
            "student_id":"1009"
        }

#inserting the data into the database collection
stu_Fred_id = collection.insert_one(student_Fred).inserted_id
stu_Jane_id = collection.insert_one(student_Jane).inserted_id
stu_West_id = collection.insert_one(student_West).inserted_id

#----1/2 OF PART ONE COMPLETE


#new documents created with firstnames and now printed document ids (no first or last names or internal student IDs)
print(stu_Fred_id)
print(stu_Jane_id)
print(stu_West_id)

#----2/2 OF PART ONE COMPLETE
