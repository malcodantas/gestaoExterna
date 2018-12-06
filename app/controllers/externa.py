from flask import render_template,redirect,request
from flask_login import login_required,current_user
from app import app,db
from app.models.tables import Equipamento
from app.models.forms import ChBox
@app.route("/retirada",methods=['GET', 'POST'])
@login_required
def emprestar():
    form=ChBox()
    if form.validate_on_submit():
        listaDeEquipamentos =request.form.getlist('listaDeEquipamentos')
        nomeDeUsuario=current_user.username
        for id in listaDeEquipamentos:
            equipamento=Equipamento.query.get(id)
            equipamento.status=1
            equipamento.usuario=nomeDeUsuario
            db.session.add(equipamento)
            db.session.commit()
    equip=Equipamento.query.all()
    return render_template('retirada.html',form=form,equipamentos=equip)

    # form=ChBox()
    # equip=Equipamento.query.all()
    # return render_template("retirada.html",equipamentos=equip,form=form)

@app.route("/externa")
def exibir():
    Listaequip=Equipamento.query.all()
    return render_template('externa.html',equipamentos=Listaequip)

@app.route("/retornou/<ide>")
@login_required 
def retornou(ide):
    equip=Equipamento.query.filter_by(id=ide).first()
    user_equip_atual=equip.usuario
    if current_user.username == user_equip_atual:
        equip=Equipamento.query.filter_by(id=ide).first()
        equip.status=0
        equip.usuario=""
        db.session.add(equip)
        db.session.commit()
        Listaequip=Equipamento.query.all()
        return render_template('externa.html',equipamentos=Listaequip)
    else:
        return " Somente quem retirou o Equipamento pode devolve-lo"