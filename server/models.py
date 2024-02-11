from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

from flask import Flask

app = Flask(__name__)

db = SQLAlchemy()

class Foods(db.Model, SerializerMixin):
    __tablename__ = 'foods'

    serialize_rules = ('-home_page_search_icons.home_page',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(256))
    category = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float(range(0,30)), nullable=False)
    image = db.Column(db.String(256), default='https://i.pinimg.com/736x/ad/ca/b2/adcab2d2165598c7208bc2105b266c61.jpg')
    

    

    def __repr__(self):
        return f"<HomePage {self.title} Description: {self.description}>"


        
class Login(db.Model, SerializerMixin):
    __tablename__ = 'logins'

    serialize_rules = ('-users.login',)

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @validates('email')
    def validate_email(self, key, value):
        if not value.endswith('@example.com'):
            raise ValueError("Email must end with '@example.com'")
        return value

    def __repr__(self):
        return f"<Login {self.email}>"

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-logins.user',)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    login_id = db.Column(db.Integer, db.ForeignKey('logins.id'), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"


class Driver(db.Model, SerializerMixin):
    __tablename__ = 'drivers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String (100), nullable=False)
    contact = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=True)
    adress= db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Driver {self.name}>"