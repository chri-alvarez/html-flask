from dojos_ninjas_flask_app import app
from dojos_ninjas_flask_app.modelo.modelo_productos import Productos
from flask import render_template, redirect, request


@app.route('/productos')
def dojos():
    resultado = Productos.get_productos()
    print(resultado.json())
    return render_template('productos.html',productos=resultado.json())

@app.route('/producto/<id_producto>')
def detalle_dojo(id_producto):
    data = {
        "id": id_producto
    }
    producto = Productos.mostrar_producto(data)
    print(producto)
    return render_template('detalle_productos.html',producto=producto.json())


@app.route('/creando_producto',methods=['POST'])
def creando_producto(): 
    resultado = Productos.crear_producto(request.form)
    print(resultado)
    return redirect('/productos')


