#usr/bin/python
#  -*- coding: utf-8 -*-

print("""Las tuplas son similares a las listas, pero no se pueden modificar 
despues de creadas, son inmutables. se crean separando por (,) los elementos
que las componen """)
print("")

tupla = "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "septiembre", "Octubre", "Noviembre", "Diciembre" 

print(tupla)


print("""Para distinguir una tupla constituida por un solo elemento de una variable, se debe poner una coma detrás de ese elemento""")
print("")

variable = 1
tupla_un_elemento = 1,

print(tupla_un_elemento)
print(type(tupla_un_elemento))
print(variable)
print(type(variable))

print("""Por buenas practivas se recomienda usar parentesis al escribir una tupla, esto ayuda a que el codigo sea muchoa mas legible""")
print("")

tupla = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "septiembre", "Octubre", "Noviembre", "Diciembre")
print("")

print("""Para aceder a la tupla se usa los corchetes indicando la posicion""")
print("")

print(tupla[3]) # muestra Abril
print(tupla[3:6]) # muestra Abril, Mayo; Junio
print(tupla[:6]) # Imprime desde Enero a Junio
print(tupla[6:]) # Imprime desde Julio a diciembre
print(tupla[::2]) # Imprime los meses de dos en dos