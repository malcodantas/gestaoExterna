from flask import render_template,redirect,flash,url_for
from flask_login import login_required
from app import app,db
from app.models.tables import User,Equipamento,Funcionario
from app.models.forms import EquipForm,FuncionariosForm,LoginForm
from werkzeug.security import generate_password_hash

@app.route("/cadastrar_usuario",methods=["GET","POST"])
@login_required
def cadastrar_usuario():
    return "cadastrar usuario"
    #render_template('cadastrar_usuario.html')
 
@app.route("/cadastrar_equipamento",methods=['POST','GET'])
@login_required
def cadastrar_equipamento():
    form=EquipForm()
    if form.validate_on_submit():
        new_equip=Equipamento(form.name.data,False,form.descricao.data)
        db.session.add(new_equip)
        db.session.commit()
        Listaequip=Equipamento.query.all()
        return render_template('externa.html',equipamentos=Listaequip)
    return render_template('cadastrar_equipamento.html',formulario=form)


@app.route("/cadastrar_funcionario",methods=["GET","POST"])
@login_required
def cadastrar_funcionario():
    form=LoginForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            print("Usuário ja existe, tente outro")
        else:
            print("usuario cadastrado")           
            novo_funcionario=User(form.username.data, generate_password_hash(form.password.data))
            db.session.add(novo_funcionario)    
            db.session.commit()
    return render_template('cadastrar_funcionario.html',formulario=form)