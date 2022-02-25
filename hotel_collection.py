from dbclient import DBClient
from bson import ObjectId
import datetime
import helpers



class HotelCollection:

    __collection = None    

    @classmethod
    def read(self, name=None, city=None, email=None):
        self.connect()
        if name is not None:
            hotels = self.__collection.find({"name": name})
        elif city is not None:
            hotels = self.__collection.find({"city": city})
        elif email is not None:
            hotels = self.__collection.find({"email": email})
        else:
            hotels = self.__collection.find()

        return [{item: data[item] for item in data if item != '_id'} for data in hotels]
    
    @classmethod
    def write(self, data):
        self.connect()

        hotel = self.__collection.insert_one({
            "name": helpers.contain_numbers(data['name'], 'Name'), 
            "city": helpers.contain_numbers(data['city'], 'City'), 
            "address": data['address'], 
            "email": data['email'], 
            "image": data['image'],
            "created_at": datetime.datetime.utcnow()
        })

        return str(hotel.inserted_id)
        
    @classmethod
    def delete(self, hotel_id):
        self.connect()
        hotel = self.__collection.delete_one({"_id": ObjectId(hotel_id)})
    
    @classmethod
    def connect(self):
        if self.__collection is None:
            db = DBClient.connnect()
            self.__collection = db['hotels']

