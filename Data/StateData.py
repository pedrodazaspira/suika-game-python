from pymongo import MongoClient
from Config import *
from bson import ObjectId
from Data.UserData import *
# Conexión a la base de datos MongoDB
db = client.get_database()

class StateData:

    def __init__(self, code, description, modifiedAt):
        self.code = code
        self.description = description
        self.modifiedAt = modifiedAt

    def setId(self, id):
        self.id = id

    
    def to_dict(self):
        return {
            "code": self.code,
            "description": self.description,
            "modifiedAt": self.modifiedAt
        }
    
    @classmethod
    def from_dict(cls, dic):
        return cls(
            code=dic.get('code'),
            description=dic.get('description'),
            modifiedAt=dic.get('modifiedAt')
        )
    
def insertStateData(stateData):
    states_collection = db["States"]
    result = states_collection.find_one({"description": stateData.description})
    if not result:
        states_collection.insert_one(stateData.to_dict())