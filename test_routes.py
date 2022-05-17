from create_app import db
from app import app
import pytest
import os, tempfile
from models import Course

student = {
    'term': 'Term 1',
    'course': 'ACIT 1420 - Introduction to Systems Administration',
    'grade':99
}

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    client = app.test_client()
    db.init_app(app)

    with app.app_context():
        db.create_all()

    yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


def test_term(client):
    rv = client.get('/gpa/B01272952')
    assert rv.status_code == 200
    with app.app_context():
        newgrade = Course(
            student_id='B01272954',
            class_name='ACIT 1420 - Introduction to Systems Administration',
            grade=100,
            class_credit=4.0
        )
        db.session.add(newgrade)
        db.session.commit()
   
        s1 = client.post('/gpa/B01272954', data=student)
        s2 = client.post('/gpa/B01272958', data=student)
        r2 = client.get('/gpa/B01272958')
        

        Course.query.filter(Course.student_id == 'B01272954').delete()
        Course.query.filter(Course.student_id == 'B01272958').delete()
        db.session.commit()

def test_view(client):
    with app.app_context():
        req = client.post('/gpa/B01272958', data=student)
        res = client.get('/gpa/B01272958')
        assert res.status_code == 200
        Course.query.filter(Course.student_id == 'B01272958').delete()
        db.session.commit()
        


   