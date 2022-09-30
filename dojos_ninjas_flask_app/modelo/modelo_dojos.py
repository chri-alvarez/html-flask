from tkinter import INSERT
from dojos_ninjas_flask_app.configuracion.mysqlconnection import connectToMySQL

class Dojos:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.crado_en = data['creado_en']
        self.actualizado_en = data['actualizado_en']

    @classmethod
    def crear_dojos(cls, data):
        query = "INSERT INTO dojos (nombre) VALUES (%(nombre)s);"
        resultado = connectToMySQL('dojos_ninjas').query_db(query, data)
        return resultado

    #METODO SOLO DE LECTURA
    @classmethod
    def mostrar_dojos(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        resultado = connectToMySQL('dojos_ninjas'). query_db(query, data)
        return resultado[0]
    
    @classmethod
    def todos_dojos(cls):
        query = "SELECT * FROM dojos;"
        resultado = connectToMySQL('dojos_ninjas'). query_db(query)
        return resultado


