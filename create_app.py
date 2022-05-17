from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

from flask_login import(
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.login_message_category = "info"

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)

    app.secret_key = 'secret-key'
    # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///gpa.db"
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://vqoqgjrohhkjig:92df98ea3edaecc90feeddbfea75152c85d97644e0afc31a409a66790d0c01c0@ec2-54-86-224-85.compute-1.amazonaws.com:5432/d90h1igebdvc8v"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)
    bcrypt.init_app(app)

    return app