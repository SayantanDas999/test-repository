# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 00:45:47 2020

@author: Sayantan
"""

from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message":"store not found"}, 404
    
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message":"store with the same name already exists"}, 400
        store=StoreModel(name)
        store.save_to_db()
        return store.json(), 201
    
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {"message":"store deleted successfully"}
            
    
    
class StoreList(Resource):
    def get(self):
        storelist = []
        stores = StoreModel.query.all()
        for store in stores:
            storelist.append(store.json())
        return {"storelist":storelist}