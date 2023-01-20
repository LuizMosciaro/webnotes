from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'Test123'
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://${{ MYSQLUSER }}:${{ MYSQLPASSWORD }}@${{ MYSQLHOST }}:${{ MYSQLPORT }}/${{ MYSQLDATABASE }}"
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_message = u'Para acessar faça login ou cadastre-se'
    login_manager.login_message_category = 'Attention: '
    login_manager.login_view = 'auth.login'

    from .views import views
    from .auth import auth
    from .models import User

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

