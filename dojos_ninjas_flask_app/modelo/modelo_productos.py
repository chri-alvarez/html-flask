#from tkinter import INSERT
#from dojos_ninjas_flask_app.configuracion.mysqlconnection import connectToMySQL
import requests

class Productos:
    def __init__(self, data):
        self.tipo = data['tipo']
        self.serie = data['serie']
        self.marca = data['marca']
        self.codigo = data['codigo']
        self.nombre = data['nombre']
        self.stock = data['stock']
        self.precio = data['precio']

    @classmethod
    def crear_producto(cls, data):
        res = requests.post('http://localhost:5001/Productos',json=data)
        return res

    #METODO SOLO DE LECTURA
    @classmethod
    def mostrar_producto(cls,data):
        res = requests.get('http://localhost:5001/Producto/'+data['id'])
        return res
    
    @classmethod
    def get_productos(cls):
        res = requests.get('http://localhost:5001/Productos')
        return res


