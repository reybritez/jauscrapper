from flask import Flask, redirect, url_for, render_template, request, flash
from models import db, Producto
from formularios import FormularioProducto

# Creo la base
app = Flask(__name__)
app.config["SECRET_KEY"] = "hasd123a"
app.config["DEBUG"] = False

# Conexión SQL
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Ruta de inicio
@app.route("/")
def index():
    """
    Home / Inicio
    """
    return redirect(url_for("productos"))


# Página Productos
@app.route("/productos")
def productos():
    """
    Muestra todos los productos
    """
    productos = Producto.query.order_by(Producto.nombre_producto).all()
    return render_template("web/productos.html", productos=productos)


@app.route("/buscar")
def buscar():
    """
    Realiza una busqueda
    """

    buscar_nombre = request.args.get("nombre")
    todos_los_productos = (
        Producto.query.filter(Producto.nombre_producto.contains(buscar_nombre))
        .order_by(Producto.nombre)
        .all()
    )
    return render_template("web/productos.html", productos=todos_los_productos)


@app.route("/agregar_producto", methods=("GET", "POST"))
def agregar_producto():
    """
    Función para crear nuevo producto
    """
    form = FormularioProducto()
    if form.validate_on_submit():
        mi_producto = Producto()
        form.populate_obj(mi_producto)
        db.session.add(mi_producto)
        try:
            db.session.commit()
            # Notificacion
            flash("Producto creado con éxito", "success")
            return redirect(url_for("productos"))
        except:
            db.session.rollback()
            flash("Error creando producto.", "danger")

    return render_template("web/agregar_producto.html", form=form)


# Funcion para Editar Productos
@app.route("/editar_producto/<id_producto>", methods=("GET", "POST"))
def editar_producto(id_producto):
    """
    Editar producto y cambiarle el precio

    :param id_producto: Id del producto
    """
    mi_producto = Producto.query.filter_by(id_producto=id_producto).first()
    form = FormularioProducto(obj=mi_producto)
    if form.validate_on_submit():
        try:
            # Se actualiza con los nuevos datos
            form.populate_obj(mi_producto)
            db.session.add(mi_producto)
            db.session.commit()
            # Le avisa al usuario a través de flash
            flash("Guardado exitosamente", "success")
        except:
            db.session.rollback()
            flash("Hubo un error editando este producto.", "danger")
    return render_template("web/editar_producto.html", form=form)


@app.route("/productos/eliminar", methods=("POST",))
def eliminar_producto():
    """
    Funcion para Eliminar Producto
    """
    try:
        mi_producto = Producto.query.filter_by(
            id_producto=request.form["id_producto"]
        ).first()
        db.session.delete(mi_producto)
        db.session.commit()
        flash("Se ha borrado exitosamente.", "danger")
    except:
        db.session.rollback()
        flash("Error borrando producto.", "danger")

    return redirect(url_for("productos"))
