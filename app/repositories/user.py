from typing import Optional
from .models import User
from werkzeug.security import safe_str_cmp

"""Base fixa de usuários"""
users = [
    User(1, 'joao', '123456'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def authenticate(username: str, password: str) -> Optional[User]:
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user


def identity(payload: any) -> Optional[User]:
    user_id = payload['identity']
    return userid_table.get(user_id, None)