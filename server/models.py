from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()

class HomePage(db.Model, SerializerMixin):
    __tablename__ = 'home_pages'

    serialize_rules = ('-home_page_search_icons.home_page',)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(256))

    home_page_search_icons = db.relationship('SearchIcon', backref='home_page')

    def __repr__(self):
        return f"<HomePage {self.title} Description: {self.description}>"

class SearchIcon(db.Model, SerializerMixin):
    __tablename__ = 'search_icons'

    serialize_rules = ('-home_page_search_icons.search_icon',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    home_page_id = db.Column(db.Integer, db.ForeignKey('home_pages.id'), nullable=False)

    @validates('url')
    def validate_url(self, key, value):
        if not value.startswith('http'):
            raise ValueError("URL must start with 'http'")
        return value

    def __repr__(self):
        return f"<SearchIcon {self.name} URL: {self.url}>"

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


