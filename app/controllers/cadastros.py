from flask import render_template,redirect,flash,url_for
from flask_login import login_required
from app import app,db
from app.models.tables import User,Equipamento,Funcionario
from app.models.forms import EquipForm,FuncionariosForm
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
def cadastrar_funcionario():
    form=FuncionariosForm()
    if form.validate_on_submit():
        if Funcionario.query.filter_by(name=form.name.data).first():
            print("Usuário ja existe, tente outro")
        else:
            print("usuario cadastrado")
            novo_funcionario=Funcionario(form.name.data,form.funcao.data)
            db.session.add(novo_funcionario)
            db.session.commit()
    #return render_template('cadastrar_funcionario.html',formulario=form)
    return "Função em desenvolvimento"