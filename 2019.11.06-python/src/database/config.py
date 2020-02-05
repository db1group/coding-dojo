from mongoengine import connect
from pymongo import MongoClient

MongoClient("mongodb://127.0.0.1:27017/talk-scheduling")
connect('talk-scheduling')
