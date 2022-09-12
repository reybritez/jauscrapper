from flask import Flask, redirect, url_for, render_template, request, flash
from models import db, Producto

#Creo la base
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hasd123a'
app.config['DEBUG'] = False

#Conexión SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

#Ruta de inicio
@app.route("/")
def index():
    '''
    Home / Inicio
    '''
    return redirect(url_for('productos'))


#Página Productos
@app.route("/productos")
def productos():
    '''
    Muestra todos los productos
    '''
    productos = Producto.query.order_by(Producto.nombre).all()
    return render_template('web/productos.html', productos=productos)


@app.route("/buscar")
def buscar():
    '''
    Realiza una busqueda
    '''

    buscar_nombre = request.args.get('nombre')
    todos_los_productos = Producto.query.filter(
        Producto.nombre.contains(buscar_nombre)
    ).order_by(Producto.nombre).all()
    return render_template('web/productos.html', productos = todos_los_productos)