from pymongo import MongoClient
from pprint import pprint

"""
	See the following for reference:
		- https://docs.mongodb.com/
		- https://docs.mongodb.com/drivers/pymongo
		- https://docs.mongodb.com/python/current/api/
		- https://docs.mongodb.com/python/current/tutorial.html
"""

url = input("What's the database URL? ")
if len(url) == 0:
	client = MongoClient()
else:
	client = MongoClient(url)

database_name = input("What's the database name? ")
db = client[database_name]

collection_name = input("What's the collection name? ")

MAX_RESULTS = 10
result = db[collection_name].find().limit(MAX_RESULTS)
totalCount = db[collection_name].count_documents({})

print("\n\n")
print("The " + database_name + "." + collection_name + " collection has " + str(totalCount) + " documents!")
if totalCount > MAX_RESULTS:
	print("Only showing the first " + str(MAX_RESULTS) + " results.")
print("\n")

resultCount = 0
for individual in result:
	pprint(individual)
	print("\n")
	resultCount += 1

print("\n")
print("Query resulted in " + str(resultCount) + " findings!")
