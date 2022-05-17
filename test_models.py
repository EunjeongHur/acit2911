from venv import create
import pytest
import os
from models import User, Course
from wtforms import ValidationError
import forms, routes
from create_app import create_app, db

@pytest.fixture
def mock_user():
    newuser = User(
        student_id = "A12345678",
        username = "User Name",
        pwd = "password"
        )
    return newuser

@pytest.fixture
def mock_course():
    newcourse = Course(
        student_id = "A12345678",
        class_name = "acit1420",
        class_credit = 4.0,
        grade = 60
    )
    return newcourse

def test_user(mock_user):
    assert mock_user.student_id =="A12345678"
    assert mock_user.username == "User Name"
    assert mock_user.pwd == "password"
    assert mock_user.is_authenticated
    assert mock_user.is_active

def test_user_repr(mock_user):
    test_repr = repr(mock_user)
    assert test_repr == '<User: User Name>' 

def test_course(mock_course):
    assert mock_course.student_id == "A12345678"
    assert mock_course.class_name == "acit1420"
    assert mock_course.class_credit == 4.0
    assert mock_course.grade == 60

def test_course_repr(mock_course):
    test_repr = repr(mock_course)
    assert test_repr == '<Grade: 60>'


