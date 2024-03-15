from ..models import User

def get_users():
    users = User.objects.get.all()
    return users

