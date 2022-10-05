from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange


class FormularioProducto(FlaskForm):
    nombre_producto = StringField(
        "Nombre",
        validators=[
            DataRequired(),
            Length(min=-1, max=80, message="No puede tener más de 80 caracteres"),
        ],
    )
    detalles_producto = StringField(
        "Detalles",
        validators=[
            DataRequired(),
            Length(min=-1, max=80, message="No puede tener más de 80 caracteres"),
        ],
    )
    cantidad_producto = IntegerField(
        "Cantidad",
        validators=[
            NumberRange(
                min=-1, max=10000000, message="No puede costar más de 10 millones"
            )
        ],
    )


class FormularioUbicacion(FlaskForm):
    nombre_ubicacion = StringField(
        "Nombre",
        validators=[
            DataRequired(),
            Length(min=-1, max=80, message="No puede tener más de 80 caracteres"),
        ],
    )


class FormularioMoverProducto(FlaskForm):
    nombre_mp = SelectField('Nombre del Producto')
    desde_mp = SelectField('Mover Desde')
    hasta_mp = SelectField('Mover A')
    cantidad_a_mover = IntegerField(
        'Cantidad', validators=[NumberRange(min=1, max=10000000), DataRequired()])
