# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 23:46:24 2020

@author: Sayantan
"""

from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_claims, jwt_optional, get_jwt_identity
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
            return {"message":"An item with the same name already exists"}, 401
        data = request.get_json()
        item=ItemModel(name,data['price'],data['store_id'])
        item.save_to_db()
        return item.json()

    @jwt_required
    def delete(self, name):
        claims = get_jwt_claims()
        if not claims["is admin"]:
            return {"message":"Admin priviledge required"}, 401
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
    @jwt_optional
    def get(self):
        user_id = get_jwt_identity()
        itemlist = []
        items = ItemModel.query.all()
        if user_id:
            for item in items:
                itemlist.append(item.json())
            return {"itemlist":itemlist}
        else:
            for item in items:
                itemlist.append(item['name'])
            return {"itemlist":itemlist , "message":"More details available if you log in"}
    
        
