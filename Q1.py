import pymongo
from bson.son import SON

client = pymongo.MongoClient()
db = client['Movies_database']
movies = db.movies
ratings = db.ratings
tags = db.tags

# Q1
cursor = db.movies.find({"Title": {'$regex': 'copycat', '$options': 'i'}})
for doc in cursor:
    print(doc['Genres'])
