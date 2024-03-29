from django.conf import settings 
import pymongo
from bson import ObjectId


class ClassroomRepository:

    def __init__(self, name) -> None:
        self.collection = name
    
    def __get_connection(self):
        MONGO_CONNECTION_STRING = getattr(settings, "MONGO_CONNECTION_STRING")
        MONGO_DATABASE_NAME = getattr(settings, "MONGO_DATABASE_NAME")

        client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
        connection = client[MONGO_DATABASE_NAME]
        return connection
    
    def __get_collection(self):
        conn = self.__get_connection()
        collection = conn[self.collection]
        return collection
    
    #CRUD

    def list(self):
        document = self.__get_collection().find({})
        return document
    
    def getById(self, document_id):
        document = self.__get_collection().find({"_id": ObjectId(document_id)})
        return document
        
    def filterByAttribute(self, attribute, value):
        if attribute in ('id', '_id'):
            return self.getById(value)

        documents = self.__get_collection().find({attribute: value})
        return list(documents)
        
    def insert(self, document) -> None:
        self.__get_collection().insert_one(document)

    def update(self, document_id, update_data):
        self.__get_collection().update_one(
            {"_id": ObjectId(document_id)},
            {"$set": update_data}
        )
        
    def delete(self, document_id) -> None:
        self.__get_collection().delete_one({"_id": ObjectId(document_id)})
 
