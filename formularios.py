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

class MoverProducto(FlaskForm):
    nombre_producto_a_mover = SelectField(
        'Product Name'
    )
    salida_desde = SelectField(
        'Source'
    )
    entrada_a = SelectField(
        'Destination'
    )
    cantidad_a_mover = IntegerField(
        'Quantity',
        validators=[
            NumberRange(
                min=1, max=10000000, message="No se puede mover más 1 millón de productos al mismo tiempo"
            )
        ],
    )