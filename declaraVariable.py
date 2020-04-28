#!/usr/bin/python
# -*- coding: utf-8 -*-

# una variable es una contenedor que guarda infoamcion 
# en la memoria, la cual podemos recuperar y usar a 
# a lo largo del programa. 

# para crear una variable solo es necesrio escribir el nombre
# que deseamos para la variable, teniendo en cuenta siertas reglas:
# * El nombre de una variable no debe contener espacios.
# * debe iniciar por una letra o por un guion bajo.
# * python distingue entre mayusculas y minusculas.
# * no se puede usar palabras reservadas:
#       and, assert, break, class, continue, def, del, elif, 
#       else, except, exec, finally, for, from, global, if, 
#       import, in, is, lambda, not, or, pass, print, raise, 
#       return, try, while.
# * no debe iniciar con un numero.
# y por buenas practica debe ser un nombre que describa la 
# funcion de la variable, var1, var2 etc no indican que
# se quiere con la variable

# para asignar el valor a una variable se usa el signo "="

variable = 20

print(variable) # esto imprime el valor de la variable osea 20.

print("") # Esto crea un espacio entre lineas

# Si se quiere declarar varias variables se puede escribir 
# separados por ","

variableUno, variableDos, variableTres = "1", 2, "3"

print(variableUno)
print(variableDos)
print(variableTres)
print("")

# las lines y los espacios en blanco generen legibiliadad del codigo: 
# es buena practica utilizarlos


# Una variable puede cambiar su "contenido" durante el programa.
# para asignar un valor a una varia solo hay que igualar la 
# varianle al nuevo valor

saludo = "Hola Mundo"
despedida = "Adios Mundo"

print(saludo) # esto imprime "Hola Mundo"
print(despedida) # esto imprime "Adios Mundo"
print("")

saludo = despedida

print(saludo) #e esto imprime "Adios Mundo"
print("")

# Las variables nos permietn tambie realizar operaciones.

numero = 6
suma = numero + 2

print(suma) # esto imprime el valor de suma que es la suma de 6 y 2
print("")

numero = 10
division = numero / 5 

print(division)
print("")

# En python al asignar un valor a una variable inplicitambte le asigno un tipo
# de dato a esa variable, esto define como se comparta python con la misma.

numero1 = 35
numero2 = 15

palabra1 = "Hola "
palabra2 = "mundo!"

print("suma de numero1 mas numero2")
print(numero1 + numero2)
print("")
print("concatenacion (union) de dos cadenas de texto")
print(palabra1 + palabra2)

# python es fuertemente tipado, lo que significa que no se puede mezclar 
# tipos de datos libremente. Por lo tanto intentar sumar una cadena de 
# texto con un numero dara error.
#    * Traceback (most recent call last):
#    *   File "declaraVariable.py", line 95, in <module>
#    *     print(numero1 + palabra1)
#    * TypeError: unsupported operand type(s) for +: 'int' and 'str'


print(numero1 + pala)
