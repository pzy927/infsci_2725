import pymongo
from bson.son import SON

client = pymongo.MongoClient()
db = client['Movies_database']
movies = db.movies
ratings = db.ratings
tags = db.tags

# Q6a
pipeline = [
    {'$group': {'_id': '$MovieID', 'count': {'$sum': 1}}},
    {'$sort': SON([('count', -1)])},
    {'$limit': 1}
]
for doc in ratings.aggregate(pipeline):
    print (movies.find_one({'MovieID': doc['_id']})['Title'])


# Q6b
pipeline = [
    {'$group': {'_id': '$UserID', 'count': {'$sum': 1}}},
    {'$sort': SON([('count', -1)])},
    {'$limit': 1}
]
for doc in ratings.aggregate(pipeline):
    print ('The most active userid = ' + str(doc['_id']))

# Q6c
pipeline = [
    {'$group': {'_id': '$Tag', 'count': {'$sum': 1}}},
    {'$sort': SON([('count', -1)])},
    {'$limit': 1}
]
for doc in tags.aggregate(pipeline):
    print(doc['_id'])
