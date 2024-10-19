import pymongo

host = pymongo.MongoClient("mongodb://cluster0-shard-00-01.zwhtg.mongodb.net:27017/")
db = host["ifheroes"]
col = db["website"]

x = col.find_one()

print(x)