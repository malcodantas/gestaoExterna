from app import app,db
from flask import render_template,redirect,url_for
from flask_login import login_user,logout_user,login_required,current_user
from app.models.forms import LoginForm,EquipForm
from app.models.tables import User,Equipamento

@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route("/login",methods=['POST','GET'])
def login():
    form=LoginForm() 
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user and user.password==form.password.data:
            login_user(user)
            return redirect(url_for('exibir'))
        else:
            pass
    return render_template('login.html',formulario=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('login')

################################################
# Gerenciamento do cadastro de equipamentos e usuários
from app.controllers import cadastros

################################################
# Gerenciamento das rotas das páginas EXTERNA, e RETIRADA
from app.controllers import externa

