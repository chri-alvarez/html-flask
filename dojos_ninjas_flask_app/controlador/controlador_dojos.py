from dojos_ninjas_flask_app import app
from dojos_ninjas_flask_app.modelo.modelo_dojos import Dojos
from dojos_ninjas_flask_app.modelo.modelo_ninjas import Ninjas
from flask import render_template, redirect, request


@app.route('/dojos')
def dojos():
    resultado = Dojos.todos_dojos()
    print(resultado)
    return render_template('dojos.html',dojos=resultado)

@app.route('/dojos/<id_dojo>')
def detalle_dojo(id_dojo):
    data = {
        "id": id_dojo
    }
    ninjas = Ninjas.todos_ninjas(data)
    dojo = Dojos.mostrar_dojos(data)
    print(ninjas)
    return render_template('detalle_dojos.html',ninjas=ninjas,dojo=dojo)


@app.route('/creando_dojos',methods=['POST'])
def creando_dojos(): 
    resultado = Dojos.crear_dojos(request.form)
    print(resultado)
    return redirect('/dojos')


