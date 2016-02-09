import pymongo
from bson.son import SON

client = pymongo.MongoClient()
db = client['Movies_database']
movies = db.movies
ratings = db.ratings
tags = db.tags

# Q2
pipeline = [
    {'$unwind': '$Genres'},
    {'$group': {'_id': '$Genres', 'count': {'$sum': 1}}},
    {'$sort': SON([('count', -1)])},
    {'$limit': 1} 
]
for doc in movies.aggregate(pipeline):
    print(doc)
