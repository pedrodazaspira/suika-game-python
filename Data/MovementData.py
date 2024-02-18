from pymongo import MongoClient
from Config import *
from bson import ObjectId
from Data.UserData import *
from Data.StateData import *
import time
# Conexión a la base de datos MongoDB
db = client.get_database()

class MovementData:

    def __init__(self, user, stateData, modifiedAt) :
        self.user = user
        self.stateData = stateData
        self.modifiedAt = modifiedAt

    def setId(self, id):
        self.id = id

    
    def to_dict(self):
        return {
            "user": ObjectId(self.user.id),
            "stateData": ObjectId(self.stateData.id),
            "modifiedAt": self.modifiedAt
        }
    
    @classmethod
    def from_dict(cls, dic):
        return cls(
            user=UserData.from_dict(dic.get["user"]),
            stateData=StateData.from_dict(dic.get('stateData')),
            modifiedAt=dic.get('modifiedAt')
        )
    
def insertEnroll(user, stateData, date):
    fecha_legible = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(date))
    movement_collection = db["Movements"]
    movementData = MovementData(user, stateData, fecha_legible)
    movement_collection.insert_one(movementData.from_dict())

def movemntUserActive(user):
    movement_collection = db["Movements"]
    userSave = validateUser(user)
    if userSave:
        stateData = StateData("ACT", "Activo", )
        fecha_legible = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time()))
        movementData = MovementData(userSave, stateData, fecha_legible)
        movement_collection.insert_one(movementData.to_dict())