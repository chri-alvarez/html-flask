from dojos_ninjas_flask_app import app
from dojos_ninjas_flask_app.controlador import controlador_productos



if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug = True)
    