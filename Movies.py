import sys
import pymongo
from pymongo import MongoClient
from sys import stdin

client = MongoClient()
db = client['Movies_database']
movies = db['movies']

for line in stdin:
	line = line.strip()
	movieId, title, genres = line.split('::')
	genres_list = genres.strip().split('|')
	doc = {"MovieID": int(movieId), "Title": title, "Genres": genres_list}
	movies.insert_one(doc)