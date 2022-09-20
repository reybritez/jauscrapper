# La idea de este script es recargar tablas cada que se ejecute

from models import db, Producto, Ubicacion, Movimiento, Balance

# from faker import Factory ##Es un rellenador de formularios demo

# fake = Factory.create('es_ES')

db.drop_all()
db.create_all()

# Crear 100 productos de prueba

# for i in range(100):
#     nombre_producto = f"Pilsen Lata Pack x {i}"
#     detalles_producto = f"Detalle {i}"
#     cantidad_producto = 1 + (i * 10)

#     # Guardar en la base de datos
#     producto_unitario = Producto(
#         nombre_producto=nombre_producto,
#         detalles_producto=detalles_producto,
#         cantidad_producto=cantidad_producto,
#     )
#     db.session.add(producto_unitario)


db.session.commit()
