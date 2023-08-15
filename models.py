from flask_login import UserMixin
from factory import db, bcrypt


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    librarian = db.Column(db.Boolean, nullable=False, default=False)
    books = db.relationship("Book", backref="owner", lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")

    def __repr__(self):
        return f"<User {self.username}>"

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password, password)


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
