from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,TextField
from wtforms.validators import DataRequired
class LoginForm(FlaskForm):
    username=StringField("username",validators=[DataRequired()])
    password=PasswordField("password",validators=[DataRequired()])
class EquipForm(FlaskForm):
    name=StringField("name",validators=[DataRequired()])
    marca=StringField("marca",validators=[DataRequired()])
    descricao=StringField("descricao")