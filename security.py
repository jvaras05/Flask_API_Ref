from werkzeug.security import safe_str_cmp
from resources.user import UserModel

#users = [User(1, 'bob', 'asdf')]
#username_mapping = { u.username: u for u in users}
#userid_mapping = { u.id: u for u in users}


def authenticate(username, password):
    #user = username_mapping.get(username, None)
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password): #other way to compare strings
        return user

def identity(payload):
    print(payload)
    user_id = payload['identity']
    #return userid_mapping.get(user_id, None)
    return UserModel.find_by_id(user_id)

