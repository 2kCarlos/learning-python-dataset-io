from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
db = client["local-test-database"]

db.players.insert({
	"username": "Whoa531",
	"worldPosition": {
		"x": 30,
		"y": 94,
		"z": 100
	}
})

result = db.players.find_one()
pprint(result)

print("!")