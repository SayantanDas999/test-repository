# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 12:44:20 2020

@author: Sayantan
"""

from flask import request
from flask_restful import Resource
from models.user import UserModel
from flask_jwt_extended import create_access_token, create_refresh_token

  
class UserRegister(Resource):
    def post(self):
        data = request.get_json()
        if UserModel.find_by_username(data['username']):
            return {"message":"A user with the same username already exists"}, 400
        user = UserModel(data['username'],data['password'])
        user.save_to_db()
        return {"message":"user created successfully"}, 201
    
class User(Resource):
    def get(self,user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message":"User not found"}, 404
        return user.json()
    
    def delete(self,user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message":"User not found"}, 404
        user.delete_from_db()
        return {"message":"User deleted successfully"}
    
class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        user = UserModel.find_by_username(data['username'])
        if user and user.password == data['password']:
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {"access_token":access_token, "refresh_token":refresh_token}
        return {"message":"Invalid Credentials"}, 400
        

        
