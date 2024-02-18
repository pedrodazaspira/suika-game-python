from pymongo import MongoClient

client = MongoClient("mongodb://Armentor:L0rdv1r1l0717@54.80.226.2:27017/SuikaGame")

environment = {
    "qa": "Qa",
    "prd":"Prd",
    "all": "All"
}