from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# Define the models
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    notes = db.relationship('Note')

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# # Create the tables
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT NOT NULL,
#         email TEXT NOT NULL
#     )
# ''')

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS posts (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title TEXT NOT NULL,
#         content TEXT NOT NULL,
#         user_id INTEGER,
#         FOREIGN KEY (user_id) REFERENCES users (id)
#     )
# ''')
