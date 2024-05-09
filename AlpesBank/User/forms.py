from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [

            'name',
            'lastName',
            'cedula',
            'correo',
            'telefono',
            #'contraseña',  
            ]