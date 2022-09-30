# importar la función que devolverá una instancia de una conexión
from dojos_ninjas_flask_app.configuracion.mysqlconnection import connectToMySQL

# modelar la clase después de la tabla friend de nuestra base de datos
class Ninjas:
    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.años = data['años']
        self.dojo_id = data['dojo_id']
        self.creado_en = data['creado_en']
        self.actualizado_en = data['actualizado_en']
        
    @classmethod
    def insertar_ninjas(cls, data):
        query = "INSERT INTO ninjas (nombre,apellido,años,dojo_id) VALUES (%(nombre)s,%(apellido)s,%(años)s,%(dojo_id)s)"
        resultado = connectToMySQL('dojos_ninjas').query_db(query, data)
        return resultado

    # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        resultado = connectToMySQL('dojos_ninjas').query_db(query, data)
        return resultado[0]

    @classmethod
    def obtener_ninjas(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        resultado = connectToMySQL('dojos_ninjas').query_db(query, data)
        return resultado[0]

    @classmethod
    def todos_ninjas(cls,data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s;"
        resultado = connectToMySQL('dojos_ninjas').query_db(query, data)
        return resultado
