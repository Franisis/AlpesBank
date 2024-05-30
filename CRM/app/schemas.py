from pydantic import BaseModel, EmailStr, constr, validator
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    nombre: str
    apellido: str
    cedula: str
    correo: str
    telefono: Optional[str] = None


class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass