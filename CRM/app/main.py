from fastapi import FastAPI, HTTPException
from schemas import UserCreate, UserUpdate

from .crud import get_user_by_cedula, create_or_update_user

app = FastAPI()


@app.get("/")
def home():
    return{"message":"hello worls"}



@app.post("/user/")
async def create_user(user: UserCreate):
    db_user = get_user_by_cedula(user.cedula)
    if db_user:
        update_user = UserUpdate(
            nombre=user.nombre,
            apellido=user.apellido,
            cedula=user.cedula,
            correo=user.correo,
            telefono=user.telefono,
            last_login=user.last_login
        )
        create_or_update_user(update_user)
        return {"msg": "User updated"}
    else:
        create_or_update_user(user)
        return {"msg": "User created"}
