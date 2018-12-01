from flask import render_template,redirect
from flask_login import login_required
from app import app,db
from app.models.tables import User,Equipamento 
from app.models.forms import EquipForm
@app.route("/cadastrar_usuario")
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