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