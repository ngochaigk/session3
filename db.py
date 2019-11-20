import pymongo
from bson import ObjectId

client = pymongo.MongoClient("mongodb://hai:12345678A@cluster0-shard-00-00-rubdc.mongodb.net:27017,cluster0-shard-00-01-rubdc.mongodb.net:27017,cluster0-shard-00-02-rubdc.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.mindx

def all_bike():
    return list(db.bike.find())

def insert_new_bike(model,fee,image,year):
    db.bike.insert_one({'model':model,'fee':fee,'image':image,'year':year})
    


# db.bike.insert_one({"model":'mini','fee':450,'image':'png','year':2019})
# db.bike.insert_one({"model":'sport','fee':650,'image':'jpg','year':2018})

