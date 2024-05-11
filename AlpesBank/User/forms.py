from django import forms
from .models import User
from django.core.validators import EmailValidator, RegexValidator, MaxLengthValidator

class UserForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100, 
        validators=[MaxLengthValidator(100)],
        error_messages={'max_length': 'El nombre debe tener máximo 100 caracteres.'}
    )
    lastName = forms.CharField(
        max_length=100, 
        validators=[MaxLengthValidator(100)],
        error_messages={'max_length': 'El apellido debe tener máximo 100 caracteres.'}
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
        validators=[RegexValidator(regex=r'^\d+$', message="La cédula solo debe contener números.")],
        error_messages={'invalid': 'La cédula solo debe contener números.'}
    )

    class Meta:
        model = User
        fields = ['name', 'lastName', 'cedula', 'correo', 'telefono']
