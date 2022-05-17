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
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://zofkkmkhearmll:32d3fb1db5ad18e8e9d625d1fdf0f5300f04ba8201f7a1f6fcf84daf4e543e61@ec2-3-209-124-113.compute-1.amazonaws.com:5432/de3tvqfj7atjqc"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)
    bcrypt.init_app(app)

    return app