
import pymongo
import os
# Connect to MongoDB
client = pymongo.MongoClient(os.getenv("DB_CONNECT"))

# Get the database
db = client["library_mangement"]

# Get the collection
collection = db["student_data"]


