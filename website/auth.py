from flask import Blueprint,render_template,request,flash,url_for,redirect
from .models import User,Note
from werkzeug.security import generate_password_hash,check_password_hash
from . import db 
from flask_login import login_user,login_required,logout_user,current_user

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('Logado com sucesso', category='Sucess')
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Senha incorreta',category='Error')
        else:
            flash('Usuário não encontrado',category='Error')

    return render_template('login.html',user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Usuário já cadastrado',category='Error')
        elif len(email) < 4:
            flash('Email invalido',category='Error')
        elif len(firstName) < 2:
            flash('Nome invalido',category='Error')
        elif password1 != password2:
            flash('Senhas diferentes',category='Error')
        elif len(password1) < 3:
            flash('Senha muito pequena',category='Error')
        else:
            new_user = User(email=email,first_name=firstName,password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Usuario criado!',category='Success')
            login_user(user,remember=True)
            return redirect(url_for('views.home')) #views=documento|home=metodo
    return render_template('signup.html')