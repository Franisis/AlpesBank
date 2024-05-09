from ..models import User

def get_users():
    users = User.objects.all()
    return users

def create_user(form):
    user = form.save()
    user.save()
    return ()

def get_by_id(user_pk):
    user = User.objects.raw("SELECT * FROM user WHERE id=%s"%user_pk)[0]
    return user

