# import statements
from pymongo import MongoClient

# database connection
# connection = MongoClient('mongodb://root:admin@localhost:27017/?authSource=the_database&authMechanism=SCRAM-SHA-256')
connection = MongoClient('mongodb://localhost:27017', username = 'root', password = 'admin')
