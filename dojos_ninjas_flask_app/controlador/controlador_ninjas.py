from dojos_ninjas_flask_app import app
from flask import render_template, request, redirect
from dojos_ninjas_flask_app.modelo.modelo_ninjas import Ninjas
from dojos_ninjas_flask_app.modelo.modelo_dojos import Dojos

# El decorador "@" asocia esta ruta con la función inmediatamente siguiente


@app.route('/ninjas')
def ninjas():
    resultado = Dojos.todos_dojos()
    return render_template('ninjas.html',dojos=resultado)

@app.route('/creando_ninjas',methods=['POST'])
def creando_ninjas():
    resultado = Ninjas.insertar_ninjas(request.form)
    print(resultado)
    dojo_id = request.form['dojo_id']
    return redirect('/dojos/'+ dojo_id)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "ESTA RUTA NO FUE ENCONTRADA", 404
    #return render_template('404.html'), 404