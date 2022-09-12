from flask import Flask, redirect, url_for, render_template, request, flash
from models import db, Producto
from formularios import FormularioProducto

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

#Funcion para Editar Productos
@app.route("/editar_producto/<id>", methods=('GET', 'POST'))
def editar_producto(id):
    '''
    Editar producto y cambiarle el precio

    :param id: Id del producto
    '''
    mi_producto = Producto.query.filter_by(id=id).first()
    form = FormularioProducto(obj=mi_producto)
    if form.validate_on_submit():
        try:
            # Se actualiza con los nuevos datos
            form.populate_obj(mi_producto)
            db.session.add(mi_producto)
            db.session.commit()
            # Le avisa al usuario a través de flash
            flash('Guardado exitosamente', 'success')
        except:
            db.session.rollback()
            flash('Hubo un error editando este producto.', 'danger')
    return render_template(
        'web/editar_producto.html',
        form=form)

@app.route("/productos/eliminar", methods=('POST',))
def eliminar_producto():
    '''
    Funcion para Eliminar Producto
    '''
    try:
        mi_producto = Producto.query.filter_by(id=request.form['id']).first()
        db.session.delete(mi_producto)
        db.session.commit()
        flash('Se ha borrado exitosamente.', 'danger')
    except:
        db.session.rollback()
        flash('Error borrando producto.', 'danger')

    return redirect(url_for('productos'))