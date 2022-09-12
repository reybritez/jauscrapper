from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


class FormularioProducto(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=-1, max=80, message='No puede tener más de 80 caracteres')])
    precio = IntegerField('Precio', validators=[NumberRange(min=-1, max=10000000, message='No puede costar más de 10 millones')])