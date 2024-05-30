import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, HTTPException

from app.crud import get_user_by_cedula, create_or_update_user
from app.schemas import UserCreate, UserUpdate



app = FastAPI()


@app.get("/")
def home():
    return{"message":"hello worls"}



"""@app.post("/user/")
async def create_user(user: UserCreate):
    db_user = get_user_by_cedula(user.cedula)
    if db_user:
        update_user = UserUpdate(
            nombre=user.nombre,
            apellido=user.apellido,
            cedula=user.cedula,
            correo=user.correo,
            telefono=user.telefono
        )
        create_or_update_user(update_user)
        return {"msg": "User updated"}
    else:
        create_or_update_user(user)
        return {"msg": "1"}"""


@app.get("/user/")
async def create_user(user: UserCreate):
    
    return {"msg": "1"}


