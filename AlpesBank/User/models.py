from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30)
    correo = models.CharField(max_length=40)
    telefono= models.CharField(max_length=10)
    #document = models.CharField(max_length=60)    


    
