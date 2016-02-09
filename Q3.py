import pymongo
from bson.son import SON

client = pymongo.MongoClient()
db = client['Movies_database']
movies = db.movies
ratings = db.ratings
tags = db.tags

# Q3
cursor = movies.find_one({"Title": {'$regex': '2001: A Space Odyssey', '$options': 'i'}})['MovieID']
for item in tags.find({"MovieID": cursor, "UserID": 146}):
    print(item['Tag'])
