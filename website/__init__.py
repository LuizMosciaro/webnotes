from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_message = u'Para acessar faça login ou cadastre-se'
    login_manager.login_message_category = 'Attention: '
    login_manager.login_view = 'auth.login'

    from .views import views
    from .auth import auth
    from .models import Note,User

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    with app.app_context():
        db.create_all()
        print(' * Memory Database created')

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

