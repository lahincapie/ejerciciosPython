#usr/bin/pyhon
#  -*- coding: utf-8 -*-

print("el bucle for se usa para recorrer listas, diccionarios, y en general, los objetos que se pueden iterrar ")
print("")

print("con listas")
lista = ["amarillo", "azul", "rojo", "negro", "blanco"]
print(lista)
print("")

for color in lista:
    print(color + " es un color")

print("")
print("Con cadenas")
print("")

frase = "fake it until you make it"

print(frase)

for letra in frase[:]:
    print(letra)

print("")
print("Con diccionarios")
print("")

datos = {"Nombre" : "Bartholomew", "Apellido" : "Simpson", "Ocupación" : "Estudiante"}
print(datos)
print("")

for dato in datos:
    print(dato)

print("para imprimir la clave valor añadimos una variable adicional en el for para indicar el valor, se tiene que poner (,) para separar los valores")
print("")

for dato, valor in datos.items():
    print("{} : {}".format(dato, valor))

# si un objeto es iterable significa que puede pasar como argumento de la funcion
# iter()

iter('cadena') # cadena
iter(['a', 'b', 'c']) # lista
iter(('a', 'b', 'c')) # tupla
iter({'a', 'b', 'c'}) # conjunto
iter({'a': 1, 'b': 2, 'c': 3}) # diccionario

# Todas las llamadas anteriores regresan un objeto de tipo iterator.
# Para que nos muestre los elementos sucesivamente se usa next()

frutas = ['manzana', 'pera', 'mango']
iterador = iter(frutas)
next(iterador)
next(iterador)
next(iterador)

