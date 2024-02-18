from pymongo import MongoClient
from Config import *
from Data.MovementData import *
from Data.StateData import *
# Conexión a la base de datos MongoDB
db = client.get_database()

class UserData:

    def __init__(self, nick, email, createAt):
        self.nick = nick
        self.email = email
        self.createAt = createAt

    def setId(self, id):
        self.id = id

    def to_dict(self):
        return {
            "nick": self.nick,
            "email": self.email,
            "createAt": self.createAt,
        }
    
    @classmethod
    def from_dict(cls, user_dict):
        return cls(
            nick=user_dict.get('nick'),
            email=user_dict.get('email'),
            createAt=user_dict.get('createAt'),
        )
    

def validateUser(user):
    users_collection = db["Users"]
    result = users_collection.find_one({"nick": user.nick})
    if not result:
        result1 = users_collection.insert_one(user.to_dict())
        result2 = users_collection.find_one({"_id": result1.inserted_id})
        userSave = UserData.from_dict(result2)
        userSave.setId(str(result2["_id"]))
        return userSave
    user.setId(str(result["_id"]))
    return user


