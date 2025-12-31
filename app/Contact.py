# import mysql.connector
# from pymongo import MongoClient
from data_interactor import DB_Connection
from bson import ObjectId


class Contact:
    def __init__(self, first_name_contact, last_name_contact, phone_number_contact):
        self.id = None
        self.first_name = first_name_contact
        self.last_name = last_name_contact
        self.phone_number = phone_number_contact

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
        }


class Contact_DA:

    @staticmethod
    def create_contact(contact_info: dict):
        collection = DB_Connection.get_contects_coll()
        result = collection.insert_one(contact_info)
        print("Contact created successfully")
        return result.inserted_id


    # @staticmethod
    # def get_all_contacts():
    #     collection = DB_Connection.get_contects_coll()
    #     const = collection.find()
    #     return list(const)
    
    @staticmethod
    def get_all_contacts():
        collection = DB_Connection.get_contects_coll()
        contacts = list(collection.find())
        for c in contacts:
            c["_id"] = str(c["_id"])
        return contacts



    # @staticmethod
    # def update_contact(contact_info: dict, id):
    #     collection = DB_Connection.get_contects_coll()
    #     result = collection.update_one(
    #         {"_id": ObjectId(id)}, 
    #         {"$set": contact_info} 
    #     )
    #     const = collection.find({"_id": ObjectId(id)})
    #     if result is not None:
    #         return True, const
    #     return False

    @staticmethod
    def update_contact(contact_info: dict, id):
        collection = DB_Connection.get_contects_coll()
        result = collection.update_one({"_id": ObjectId(id)}, {"$set": contact_info})

        updated = collection.find_one({"_id": ObjectId(id)})
        if updated:
            updated["_id"] = str(updated["_id"])

        return result.modified_count > 0, updated





    @staticmethod
    def delete_contact(id):
        collection = DB_Connection.get_contects_coll()
        result = collection.delete_one({"_id": ObjectId(id)})
        print(f"Deleted count: {result.deleted_count}")
        if result is not None:
            return True
        return False 
