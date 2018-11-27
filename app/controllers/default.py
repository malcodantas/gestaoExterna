from app import app
from flask import render_template,redirect,url_for
from flask_login import login_user,logout_user,login_required

from app.models.forms import LoginForm
from app.models.tables import User
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

@app.route("/cadastrar_usuario")
def cadastrar_usuario():
    return "cadastrar usuario"
    #render_template('cadastrar_usuario.html')
 
@app.route("/cadastrar_equipamento")
def cadastrar_equipamento():
    return "cadastro de equipamento"
################################################
@app.route("/retirada")
def emprestar():
    return "Retirada"

@app.route("/externa")
def exibir():
    return render_template('externa.html')