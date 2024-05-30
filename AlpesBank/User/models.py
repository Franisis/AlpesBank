from django.db import models
from rest_framework import serializers
import json

# Create your models here.

class User(models.Model):
    id = str()
    correo = str()
    name = str()
    lastname = str()
    cedula = str()
    telefono = str()

    @staticmethod
    def from_mongo(dto):
        user = User()
        user.id = str(dto['_id'])
        user.name = dto['name']
        user.lastname = dto['lastname']
        user.telefono = dto['telefono']
        user.cedula = dto['cedula']
        user.correo = dto['correo']
        return user

    def to_dict(self):
        return {
            "id": self.id,
            "correo": self.correo,
            "name": self.name,
            "lastname": self.lastname,
            "cedula": self.cedula,
            "telefono": self.telefono
        }
