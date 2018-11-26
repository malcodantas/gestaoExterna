from app import app
from flask import render_template,redirect
from app.models.forms import LoginForm
@app.route("/")
def index():
    return "index"

@app.route("/login",methods=['POST','GET'])
def login():
    form=LoginForm() 
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    return render_template('login.html',formulario=form)


  









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
    return " mostrar equipamentos emprestados "    