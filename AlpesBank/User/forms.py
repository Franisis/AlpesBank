from django import forms
from django.core.validators import EmailValidator, RegexValidator, MaxLengthValidator, MinLengthValidator
from .models import User

class UserForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100, 
        validators=[MinLengthValidator(1), MaxLengthValidator(100)],
        error_messages={
            'max_length': 'El nombre debe tener máximo 100 caracteres.',
            'min_length': 'El nombre es un campo obligatorio.'
        }
    )
    lastName = forms.CharField(
        max_length=100, 
        validators=[MinLengthValidator(1), MaxLengthValidator(100)],
        error_messages={
            'max_length': 'El apellido debe tener máximo 100 caracteres.',
            'min_length': 'El apellido es un campo obligatorio.'
        }
    )
    correo = forms.EmailField(
        validators=[EmailValidator()],
        error_messages={'invalid': 'Por favor ingresa un correo electrónico válido.'}
    )
    telefono = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^3\d{9}$',
                message="Número de teléfono inválido. Debe comenzar con '3' y tener 10 dígitos en total."
            )
        ],
        error_messages={'invalid': 'Por favor ingresa un número de teléfono válido de Colombia.'}
    )
    cedula = forms.CharField(
        validators=[RegexValidator(regex=r'^\d{5,10}$', message="La cédula debe tener entre 5 y 10 dígitos.")],
        error_messages={'invalid': 'La cédula solo debe contener números y tener entre 5 y 10 dígitos.'}
    )

    class Meta:
        model = User
        fields = ['name', 'lastName', 'cedula', 'correo', 'telefono']
