import pymongo
__author__ = 'Centusk'


class Database(object):
    URI = 'mongodb://127.0.0.1:27017'
    DATABASE = None
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client["terminalBlog"]
    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert_one(data)
    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)
    @staticmethod
    def findOne(collection, query):
        return Database.DATABASE[collection].find_one(query)
