from django import forms
from .models import User

class UserForm(forms.ModelForm):
    model = User
    fields = [
        
        'nombre',
        'cedula',
        'correo',
        'telefono',

        ]