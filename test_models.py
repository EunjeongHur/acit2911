import pytest
from models import User, Course

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
    newuser = mock_user
    assert newuser.student_id =="A12345678"
    assert newuser.username == "User Name"
    assert newuser.pwd == "password"

def test_user_repr(mock_user):
    newuser = mock_user
    test_repr = repr(newuser)
    assert test_repr == '<User: User Name>' 

def test_course(mock_course):
    newcourse = mock_course
    assert newcourse.student_id == "A12345678"
    assert newcourse.class_name == "acit1420"
    assert newcourse.class_credit == 4.0
    assert newcourse.grade == 60

def test_course_repr(mock_course):
    newcourse = mock_course
    test_repr = repr(newcourse)
    assert test_repr == '<Grade: 60>'