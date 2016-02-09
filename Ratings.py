import sys
import pymongo
from sys import stdin
from pymongo import MongoClient
import datetime

client = MongoClient()
db = client['Movies_database']
ratings = db['ratings']

for line in stdin:
	line = line.strip()
	userId, movieId, rating, timestamp = line.split('::')
	doc = {"UserID": int(userId), "MovieID": int(movieId), "Rating": float(rating), "Timestamp": datetime.datetime.fromtimestamp(int(timestamp))}
	ratings.insert_one(doc)
