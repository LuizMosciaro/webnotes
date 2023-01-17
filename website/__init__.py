from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    application = Flask(__name__)
    application.secret_key = 'B5d0B6I1iQgDkFja$10b19fb6c173503dbbfcd58c58d65'
    application.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(application)
    
    login_manager = LoginManager()
    login_manager.init_app(application)
    login_manager.login_view = 'auth.login'

    from .views import views
    from .auth import auth
    from .models import Note,User

    application.register_blueprint(views,url_prefix='/')
    application.register_blueprint(auth,url_prefix='/')

    with application.app_context():
        db.create_all()
        print('Database created')

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return application

