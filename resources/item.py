# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 23:46:24 2020

@author: Sayantan
"""

from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from models.item import ItemModel

class Item(Resource):
    @jwt_required
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message":"item not found"}, 404
        
  
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message":"An item with the same name already exists"}, 400
        data = request.get_json()
        item=ItemModel(name,data['price'],data['store_id'])
        item.save_to_db()
        return item.json()

    
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"message":"item deleted successfully"}

  
    def put(self, name):
        data = request.get_json()
        item=ItemModel.find_by_name(name)
        if item is None:
            item=ItemModel(name,data['price'],data['store_id'])
        else:
            item.price=data['price']
            item.store_id=data['store_id']
        item.save_to_db()
        return item.json()       
    
class ItemList(Resource):
    def get(self):
        itemlist = []
        items = ItemModel.query.all()
        for item in items:
            itemlist.append(item.json())
        return {"itemlist":itemlist}
    
        
