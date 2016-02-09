import pymongo
from bson.son import SON

client = pymongo.MongoClient()
db = client['Movies_database']
movies = db.movies
ratings = db.ratings
tags = db.tags

# Q4
pipeline = [
    {'$group': {'_id': '$MovieID', 'avg_rating': {'$avg': '$Rating'}}},
    {'$sort': SON([('avg_rating', -1)])},
    {'$limit': 5}
]
for doc in ratings.aggregate(pipeline):
    print(movies.find_one({'MovieID': doc['_id']})['Title'])