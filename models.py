from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Producto(db.Model):

    __tablename__ = 'producto'

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(80), nullable = False)
    precio = db.Column(db.NUMERIC, nullable = False)

    def __repr__(self):
        return '<Productos %r' % self.nombre