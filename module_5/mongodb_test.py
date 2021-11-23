from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.wcq8x.mongodb.net/pytech?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
print(db.list_collection_names)
#this is the part I don't get, it prints out the shard URLs instead of the collection names along with other extraneous data.
#Database.list_collection_names of 
# Database(MongoClient
#   (
#   host=
#       [
#       'cluster0-shard-00-02.wcq8x.mongodb.net:27017', 
#       'cluster0-shard-00-01.wcq8x.mongodb.net:27017', 
#       'cluster0-shard-00-00.wcq8x.mongodb.net:27017'
#       ], 
#   document_class=dict, 
#   tz_aware=False, 
#   connect=True, 
#   retrywrites=True, 
#   w='majority', 
#   authsource='admin', 
#   replicaset='atlas-ircqgn-shard-0', 
#   ssl=True
#   ), 
#'pytech'
# ) <----what?