#!/usr/bin/python
# # -*- coding: utf-8 -*-

class Producto: 
    """ Ejemplo de clase con la cantidad y el precio de un pro-ducto""" 
    # el metodo __init__ es el constructor de la clase
    # se ejecuta siempre al instanciar una calse y es al que se le pasan los argumentos al crear nuestra clase
    def __init__(self,producto,precio,unidades): # el primer parametro de una clase debe ser siempre self
        
        self.producto = producto  # self es un nombre que se refiere  siempre al propio objeto
        self.precio = precio 
        self.unidades = unidades 
        
    def costo_total(self): # si un metodo solo tiene el parametro self que es obligatorio este no es necesario definirlo despues
        costo = self.precio * self.unidades 
        return costo

mi_objeto_producto = Producto("corbata",35,67)
        
print mi_objeto_producto.producto
print mi_objeto_producto.precio
print mi_objeto_producto.unidades
print mi_objeto_producto.costo_total()