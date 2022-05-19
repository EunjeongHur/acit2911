from flask import (
    Flask,
    render_template,
    redirect,
    flash,
    render_template_string,
    url_for,
    session,
    request
)

from datetime import timedelta
from sqlalchemy.exc import (
    IntegrityError,
    DataError,
    DatabaseError,
    InterfaceError,
    InvalidRequestError,
)

from sqlalchemy import and_
from werkzeug.routing import BuildError
from credit import Credit

from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash

from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)

from create_app import create_app, db, login_manager, bcrypt
from models import User, Course
from forms import login_form, register_form

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app = create_app()

@app.before_request
def session_handler():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=10)

@app.route("/", methods=("GET", "POST"), strict_slashes=False)
def index():
    return render_template("index.html")

@app.route("/gradeInput")
def gradeInput():
    return render_template("gradeInput.html")

@app.route("/gpa/<string:stu_id>")
def view(stu_id):
    student = Course.query.filter_by(student_id=stu_id).all()
    score = 0
    total_credits = 0
    if len(student) == 0:
        return render_template("gpa.html", data=student, gpa=0)
    for i in student:
        score += (i.grade * i.class_credit)
        total_credits += i.class_credit
    gpa = int(score/total_credits)
    if gpa >= 100:
        letter_grade = 'A+'
    elif gpa < 100 and gpa >= 95:
        letter_grade = 'A'
    elif gpa < 95 and gpa >= 90:
        letter_grade = 'A-'
    elif gpa < 90 and gpa >= 85:
        letter_grade = 'B+'
    elif gpa < 85 and gpa >= 80:
        letter_grade = 'B'
    elif gpa < 80 and gpa >= 75:
        letter_grade = 'B-'
    elif gpa < 75 and gpa >= 70: 
        letter_grade = 'C+'
    elif gpa < 70 and gpa >= 65:
        letter_grade = 'C'
    elif gpa < 65 and gpa >= 60:
        letter_grade = 'C-'
    elif gpa < 60 and gpa >= 55:
        letter_grade = 'D+'
    elif gpa < 55 and gpa >= 50:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    return render_template("gpa.html", data=student, gpa=gpa, letter_grade=letter_grade)


@app.route("/gpa/<string:stu_id>", methods=["POST"])
def term(stu_id):
    if request.method == 'POST':
        data = request.form.to_dict(flat=False)
        for i in data['term']:
            terms = i
        for i in data['course']:
            cname = i
        for i in data['grade']:
            grade = i
        credit = Credit(terms).find_course(cname)
        try:
            query = db.session.query(Course).filter(
                and_(
                    Course.class_name.like(cname),
                    Course.student_id.like(stu_id)
                )
            )
            length = []
            for i in query:
                length.append(i)
            if len(length) >= 1:
                raise InvalidRequestError
            else:
                newgrade = Course(
                    student_id=stu_id,
                    class_name=cname,
                    class_credit=credit,
                    grade=grade
                )

                db.session.add(newgrade)
                db.session.commit()
                return render_template("input.html")

        except DataError:
            db.session.rollback()
            flash(f"Invalid Entry", "warning")
        except InvalidRequestError:
            db.session.rollback()
            r_error=True
            return render_template("input.html", r_error=r_error)
    
@app.route("/gpa/delete/<string:stu_id>/<int:id>", methods=['POST'])
def delete(stu_id,id):
    if request.method == 'POST':
        data = request.form['delete_button']
        try:
            if data == 'Delete':
                Course.query.filter(Course.id == id).delete()
                db.session.commit()
                
                return redirect(url_for('view', stu_id=stu_id))
            else:
                print('nn')
                return render_template_string("df")
        except DataError:
            db.session.rollback()
        except AttributeError:
            db.session.rollback()

@app.route("/login/", methods=("GET", "POST"), strict_slashes=False)
def login():
    form = login_form()

    if form.validate_on_submit():
        try:
            user = User.query.filter_by(student_id=form.student_id.data).first()
            if check_password_hash(user.pwd, form.pwd.data):
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash("Invalid Student ID or password!", "danger")
        except Exception as e:
            flash(e, "danger")
    return render_template("auth.html",
    form=form, text="Login", btn_action="Login")

@app.route("/register/", methods=("GET", "POST"), strict_slashes=False)
def register():
    form = register_form()
    if form.validate_on_submit():
        try:
            student_id = form.student_id.data
            pwd = form.pwd.data
            username = form.username.data

            newuser = User(
                student_id = student_id,
                username = username,
                pwd=generate_password_hash(pwd).decode('utf8'),
            )

            db.session.add(newuser)
            db.session.commit()
            flash(f"Account Succesfully created", "success")
            return redirect(url_for("login"))

        except InvalidRequestError:
            db.session.rollback()
            flash(f"Something went wrong", "danger")
        except IntegrityError:
            db.session.rollback()
            flash(f"User already exists", "warning")
        except DataError:
            db.session.rollback()
            flash(f"Invalid Entry", "warning")
        except InterfaceError:
            db.session.rollback()
            flash(f"Error connecting to the database", "danger")
        except BuildError:
            db.session.rollback()
            flash(f"An error occured!", "danger")
    return render_template("auth.html", form=form, text="Create account", btn_action="Register Account")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=False)

