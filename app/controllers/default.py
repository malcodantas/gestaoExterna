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

@app.route("/cadastrar_usuario")
def cadastrar_usuario():
    return "cadastrar usuario"
    #render_template('cadastrar_usuario.html')
 
@app.route("/cadastrar_equipamento",methods=['POST','GET'])
def cadastrar_equipamento():
    form=EquipForm()
    if form.validate_on_submit():
        new_equip=Equipamento(form.name.data,False,form.descricao.data)
        db.session.add(new_equip)
        db.session.commit()
        Listaequip=Equipamento.query.all()
        return render_template('externa.html',equipamentos=Listaequip)
    return render_template('cadastrar_equipamento.html',formulario=form)
################################################
@app.route("/retirada")
def emprestar():
    equip=Equipamento.query.all()
    return render_template("retirada.html",equipamentos=equip)

@app.route("/externa")
def exibir():
    Listaequip=Equipamento.query.all()
    return render_template('externa.html',equipamentos=Listaequip)

@app.route("/retornou/<ide>")
def retornou(ide):
    equip=Equipamento.query.filter_by(id=ide).first()
    equip.status=0
    db.session.add(equip)
    db.session.commit()
    Listaequip=Equipamento.query.all()
    return render_template('externa.html',equipamentos=Listaequip)
@app.route("/retirar/<ide>")
def retirar(ide):
    equip=Equipamento.query.filter_by(id=ide).first()
    equip.status=1
    db.session.add(equip)
    db.session.commit()
    Listaequip=Equipamento.query.all()
    return render_template('retirada.html',equipamentos=Listaequip)

