# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 12:25:44 2020

@author: Sayantan
"""

from models.user import UserModel


def authenticate(username,password):
    user = UserModel.find_by_username(username)
    if user and user.password==password:
        return user
    
def identity(payload):
    user_id=payload["identity"]
    return UserModel.find_by_id(user_id)

