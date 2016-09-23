from pymongo import MongoClient
client = MongoClient()
#client = MongoClient("mongodb://mongodb0.example.net:27017")


db = client.local

cursor= db.local.find()

for document in cursor:
	print (document)