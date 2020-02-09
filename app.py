# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 00:49:13 2020

@author: Sayantan
"""

import os
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.user import UserRegister, User, UserLogin
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"]=True
app.secret_key = 'rivu'
api = Api(app)

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()
    
jwt = JWTManager(app)
    
api.add_resource(Item, '/items/<string:name>')
api.add_resource(Store, '/stores/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')

if __name__=='__main__':
    app.run()
    