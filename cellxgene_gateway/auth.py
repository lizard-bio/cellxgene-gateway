from cellxgene_gateway import env
from dataclasses import dataclass
import json
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash, generate_password_hash

auth = HTTPBasicAuth()

def get_auth():
    return auth


class Role:
    ADMIN = "ADMIN"
    USER = "USER"

@dataclass
class User:
    username: str
    password: str
    role: str

with open(env.user_file, 'r') as f:
  data = json.load(f)["users"]

users = dict((u["username"], User(u["username"], generate_password_hash(u["password"]), u["role"])) for u in data)

print(users)

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username).password, password):
        return username

@auth.get_user_roles
def get_user_roles(user: str):
    return users.get(user).role