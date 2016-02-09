import sys
import pymongo
from sys import stdin
from pymongo import MongoClient
import datetime

client = MongoClient()
db = client['Movies_database']
tags = db['tags']

for line in stdin:
	line = line.strip()
	userId, movieId, tag, timestamp = line.split('::')
	doc = {"UserID": int(userId), "MovieID": int(movieId), "Tag": tag, "Timestamp": datetime.datetime.fromtimestamp(int(timestamp))}
	tags.insert_one(doc)
