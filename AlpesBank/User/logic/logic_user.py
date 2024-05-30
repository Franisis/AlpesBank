from ..models import User
from django.db import connection
from pymongo import MongoClient
from bson.objectid import ObjectId
import requests


def get_users():
    client = MongoClient("mongodb://monitoring_user:isis2503@10.128.0.70:27017")
    db = client.monitoring_db
    variables_collection = db['variables']
    cursor = variables_collection.find({})
    users = [ User.from_mongo(user) for user in cursor ]
    client.close()

    return users

def get_by_id(id):
    client = MongoClient("mongodb://monitoring_user:isis2503@10.128.0.70:27017")
    db = client.monitoring_db
    variables_collection = db['users']
    user = variables_collection.find_one({'id': id})
    client.close()

    if user is None:
        raise ValueError('Variable not found')

    return User.from_mongo(user)

def verifyUserData(data):
    
    user = User()
    user.id = data['id']
    user.name = data['name']
    user.lastname = data['lastname']
    user.cedula = data['cedula']
    user.correo = data['correo']
    user.telefono = data['telefono']

    return user

def createUser(data):

    # Verify variable data
    user = verifyUserData(data)

    # Create variable in MongoDB
    client = MongoClient("mongodb://monitoring_user:isis2503@10.128.0.70:27017")
    db = client.monitoring_db
    variables_collection = db['variables']
    user.id = variables_collection.insert(
        {
            'id': str(user.id),
            'correo': user.correo,
            'name': user.name,
            'lastname': user.lastname,
            'cedula': str(user.cedula),
            'telefono': str(user.telefono)
        }
    )
    client.close()
    return user

# def get_users():
#     users = User.objects.all()
#     return users

# def create_user(form):
#     user = form.save()
#     user.save()
#     return ()

# def get_by_id(user_pk):
#     user = User.objects.get(pk=user_pk)
#     return user



