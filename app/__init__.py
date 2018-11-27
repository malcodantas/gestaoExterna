from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager,Server
from flask_login import LoginManager


app=Flask(__name__)

#configurações
app.config.from_object('config')
    #Gerenciador de login
lm=LoginManager()
lm.init_app(app)
#banco de dados
db=SQLAlchemy(app)
migrate = Migrate(app,db)
manager=Manager(app)
manager.add_command('db',MigrateCommand)
manager.add_command("runserver", Server())
    #Definindo tabelas do Banco de dados
from app.models.tables import User
from app.models import tables
from app.controllers import default
#Definindo Rotas

#definir no init
@lm.user_loader
def load_user(user_id):
    return User.query.filter(User.id==(user_id)).first()

