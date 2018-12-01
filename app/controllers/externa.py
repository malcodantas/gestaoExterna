from flask import render_template,redirect
from flask_login import login_required
from app import app,db
from app.models.tables import Equipamento
@app.route("/retirada")
@login_required
def emprestar():
    equip=Equipamento.query.all()
    return render_template("retirada.html",equipamentos=equip)

@app.route("/externa")
@login_required
def exibir():
    Listaequip=Equipamento.query.all()
    return render_template('externa.html',equipamentos=Listaequip)

@app.route("/retornou/<ide>")
@login_required
def retornou(ide):
    equip=Equipamento.query.filter_by(id=ide).first()
    equip.status=0
    db.session.add(equip)
    db.session.commit()
    Listaequip=Equipamento.query.all()
    return render_template('externa.html',equipamentos=Listaequip)
@app.route("/retirar/<ide>")
@login_required
def retirar(ide):
    equip=Equipamento.query.filter_by(id=ide).first()
    equip.status=1
    db.session.add(equip)
    db.session.commit()
    Listaequip=Equipamento.query.all()
    return render_template('retirada.html',equipamentos=Listaequip)
