# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 12:44:20 2020

@author: Sayantan
"""

from flask import request
from flask_restful import Resource
from models.user import UserModel

  
class UserRegister(Resource):
    def post(self):
        data = request.get_json()
        if UserModel.find_by_username(data['username']):
            return {"message":"A user with the same username already exists"}, 400
        user = UserModel(data['username'],data['password'])
        user.save_to_db()
        return {"message":"user created successfully"}, 201
        

        
