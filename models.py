from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Producto(db.Model):

    __tablename__ = "producto"

    id_producto = db.Column(db.Integer, primary_key=True)
    nombre_producto = db.Column(db.String(80), nullable=False)
    detalles_producto = db.Column(db.String(120), nullable=False)
    cantidad_producto = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "Productos %r" % self.nombre_producto


class Ubicacion(db.Model):

    __tablename__ = "ubicacion"

    id_ubicacion = db.Column(db.Integer, primary_key=True)
    nombre_ubicacion = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"Ubicacion('{self.id_ubicacion}', '{self.nombre_ubicacion}'"


class Movimiento(db.Model):

    __tablename__ = "movimiento"

    id_movimiento = db.Column(db.Integer, primary_key=True)
    hora_fecha_movimiento = db.Column(db.DateTime, default=datetime.utcnow())
    salida_desde = db.Column(db.String(20), nullable=False)
    entrada_a = db.Column(db.String(20), nullable=False)
    nombre_producto_a_mover = db.Column(db.String(20), nullable=False)
    cantidad_a_mover = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Movimiento('{self.hora_fecha_movimiento}', '{self.salida_desde}','{self.entrada_a}','{self.nombre_producto_a_mover}','{self.cantidad_a_mover}'"


class Balance(db.Model):

    __tablename__ = "balance"

    id_balance = db.Column(db.Integer, primary_key=True)
    nombre_producto = db.Column(db.String(20), nullable=False)
    ubicacion_producto = db.Column(db.String(20), nullable=False)
    cantidad_producto = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"('{self.nombre_producto}','{self.ubicacion_producto}','{self.cantidad_producto}')"
