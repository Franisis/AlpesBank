from ..models import User
from django.db import connection

def get_users():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM User")
        return cursor.fetchall()

# def get_users():
#     users = User.objects.all()
#     return users

def create_user(form):
    user = form.save()
    user.save()
    return ()

# def get_by_id(user_pk):
#     users = User.objects.raw("SELECT * FROM User WHERE name = %s", [user_pk])
#     user = next(iter(users), None)
#     return user

def get_by_id(user_pk):
    users = User.objects.raw("SELECT * FROM User")
    user = next(iter(users), None)
    return user


