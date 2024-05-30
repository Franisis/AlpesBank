from sqlalchemy.orm import Session
from .models import User
from .schemas import UserCreate, UserUpdate
from .database import SessionLocal


def get_user_by_cedula(cedula: str):
    db = SessionLocal()
    return db.query(User).filter(User.cedula == cedula).first()

def create_or_update_user(user: UserCreate):
    db = SessionLocal()
    db_user = db.query(User).filter(User.cedula == user.cedula).first()
    if db_user:
        db_user.nombre = user.nombre
        db_user.apellido = user.apellido
        db_user.correo = user.correo
        db_user.telefono = user.telefono
 
    else:
        db_user = User(
            nombre=user.nombre,
            apellido=user.apellido,
            cedula=user.cedula,
            correo=user.correo,
            telefono=user.telefono,
            last_login=user.last_login
        )
        db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return db_user