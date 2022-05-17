from sqlalchemy import ForeignKey
from create_app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(9), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True,nullable=False)
    pwd = db.Column(db.String(300), nullable=False, unique=True)

    def __repr__(self):
        return f'<User: {self.username}>'

class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(9), unique=False, nullable=False)
    class_name = db.Column(db.String(30), unique=False, nullable=False)
    class_credit = db.Column(db.Float, unique=False, nullable=False)
    grade = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f'<Grade: {self.grade}>'