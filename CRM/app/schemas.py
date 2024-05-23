from pydantic import BaseModel, EmailStr, constr, validator
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    nombre: constr(max_length=100)
    apellido: constr(max_length=100)
    cedula: constr(regex=r'^\d+$')
    correo: EmailStr
    telefono: Optional[constr(regex=r'^3\d{9}$')]
    last_login: Optional[datetime] = None

    @validator('nombre', 'apellido')
    def validate_max_length(cls, v):
        if len(v) > 100:
            raise ValueError('El nombre/apellido debe tener máximo 100 caracteres.')
        return v

    @validator('cedula')
    def validate_cedula(cls, v):
        if not v.isdigit():
            raise ValueError('La cédula solo debe contener números.')
        return v

    @validator('telefono')
    def validate_telefono(cls, v):
        if v and (len(v) != 10 or not v.startswith('3')):
            raise ValueError("Número de teléfono inválido. Debe comenzar con '3' y tener 10 dígitos en total.")
        return v

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass
