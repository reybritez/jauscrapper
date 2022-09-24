from flask import Flask, redirect, url_for, render_template, request, flash
from models import db, Producto, Ubicacion
from formularios import FormularioProducto, FormularioUbicacion

# Creo la base
app = Flask(__name__)
app.config["SECRET_KEY"] = "hasd123a"
app.config["DEBUG"] = True

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
    existe = bool(Producto.query.all())
    if existe == False:
        flash(
            f"Agrega productos, detalles del mismo y cantidades iniciales para agregarlos acá",
            "info",
        )
    return render_template("web/productos.html", productos=productos)


@app.route("/buscar")
def buscar():
    """
    Realiza una busqueda
    """

    buscar_nombre = request.args.get("nombre")
    todos_los_productos = (
        Producto.query.filter(Producto.nombre_producto.contains(buscar_nombre))
        .order_by(Producto.nombre_producto)
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


#### --------------- Locations --------------- ####
# Página ubicaciones
@app.route("/ubicaciones")
def ubicaciones():
    """
    Muestra todos los ubicaciones
    """
    ubicaciones = Ubicacion.query.order_by(Ubicacion.nombre_ubicacion).all()
    existe = bool(Ubicacion.query.all())
    if existe == False:
        flash(
            f"Agrega ubicaciones de almacenamiento, bodegas o depósitos",
            "info",
        )
    return render_template("web/ubicaciones.html", ubicaciones=ubicaciones)


@app.route("/agregar_ubicacion", methods=("GET", "POST"))
def agregar_ubicacion():
    """
    Función para crear nuevo ubicacion
    """
    form = FormularioUbicacion()
    if form.validate_on_submit():
        nueva_ubicacion = Ubicacion()
        form.populate_obj(nueva_ubicacion)
        db.session.add(nueva_ubicacion)
        try:
            db.session.commit()
            # Notificacion
            flash("Ubicacion creada con éxito", "success")
            return redirect(url_for("ubicaciones"))
        except:
            db.session.rollback()
            flash("Error creando ubicacion.", "danger")

    return render_template("web/agregar_ubicacion.html", form=form)


# Funcion para Editar Ubicaciones
@app.route("/editar_ubicacion/<id_ubicacion>", methods=("GET", "POST"))
def editar_ubicacion(id_ubicacion):
    """
    Editar ubicacion

    :param id_ubicacion: Id de la ubicacion
    """
    mi_ubicacion = Ubicacion.query.filter_by(id_ubicacion=id_ubicacion).first()
    form = FormularioUbicacion(obj=mi_ubicacion)
    if form.validate_on_submit():
        try:
            # Se actualiza con los nuevos datos
            form.populate_obj(mi_ubicacion)
            db.session.add(mi_ubicacion)
            db.session.commit()
            # Le avisa al usuario a través de flash
            flash("Cambio en ubicacion realizado exitosamente", "success")
        except:
            db.session.rollback()
            flash("Hubo un error editando esta ubicacion.", "danger")
    return render_template("web/editar_ubicacion.html", form=form)


@app.route("/ubicaciones/eliminar", methods=("POST",))
def eliminar_ubicacion():
    """
    Funcion para Eliminar Ubicaciones
    """
    try:
        mi_ubicacion = Ubicacion.query.filter_by(
            id_ubicacion=request.form["id_ubicacion"]
        ).first()
        db.session.delete(mi_ubicacion)
        db.session.commit()
        flash("Ubicacion borrada exitosamente.", "danger")
    except:
        db.session.rollback()
        flash("Error borrando ubicacion.", "danger")

    return redirect(url_for("ubicaciones"))
