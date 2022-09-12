#La idea de este script es recargar tablas cada que se ejecute

from models import db, Producto
#from faker import Factory ##Es un rellenador de formularios demo

#fake = Factory.create('es_ES')

db.drop_all()
db.create_all()

#Crear 100 productos de prueba

for i in range(100):
    nombre = f'Pilsen Lata Pack x {i}'
    precio = 12000 + (i * 100)

    #Guardar en la base de datos
    producto_unitario = Producto(nombre= nombre, precio = precio)
    db.session.add(producto_unitario)

db.session.commit()