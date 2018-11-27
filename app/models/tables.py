from app import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash,generate_password_hash
class User(db.Model,UserMixin):
    __tablename__="users"
    id = db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80), unique=True)
    password=db.Column(db.String(128))

    def __init__(self,username,password):
        self.username=username
        self.password=password
    def __repr__(self):
        return self.username
#class Equipamento(db.Model):
