#!/usr/bin/python
# -*- coding: utf-8 -*-

print(""" 
En Python una variable es una referencia a un dato. Lo que quiere decir que Python crea un identificador que enlaza al dato.
la funcion id() nos muestra el identificador
""")

variable1 = "Hello"
print(id(variable1))
variable2 = "Ciao"
print(id(variable2))
variable3 = "Salut"
print(id(variable3))
variable4 = "Hallo"
print(id(variable4))

print("""Cuando se copia una variable, lo que python hace es crear una nueva referencia apuntando a ese mismo dato, por lo que queda una solo variable con dos refencias distinta""")
print("")

print(variable1)
print(id(variable1))
variabl1 = variable2
print(variabl1)
print(id(variable1))
print("")
print(variable3)
print(id(variable3))
variabl3 = variable4
print(variabl3)
print(id(variable3))


print("""esto se hace asi por que es muy eficiente en terminos de memoria y velocidad: es mucho mas rapido y economico crear una referencia que copiar el contenido de la variable""")
print("")

print("""Si se modifica el contenido de la variable, Python crea una nueva refencia que apunta a la variable """)
print("")

dia = "sabado"
print(dia)
print(id(dia))
dia = "domingo"
print(dia)
print(id(dia))

print("esto funciona para numeros, valores logicos, cadenas, y tuplas a estos tipos de datos se les llama inmutables")
print("")


print("""Sin embargo, las listas, los sets y los diccionarios son mutables: sí que pueden	modificarse	realmente	sin	que	cambie	su	id.	Es	decir,	que	podemos	agregar,	quitar	o	modificar	sus	elementos	sin	que	Python	tenga	que	reescribir	toda	la	lista o diccionario.	Python	no	crea	una	lista	nueva	cada	vez	que	modificamos	alguno	de	sus	elementos. """)


lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

print(lista)
print(id(lista))
print("")
lista[0] = "Monday"
print(lista)
print(id(lista))
lista[1] = "Tuesday"
print(lista)
print(id(lista))
lista[2] = "Wednesday"
print(lista)
print(id(lista))
print("")

print("""Si hacemos una copia de un elemento inmutable, esto no afecta al original (y viceversa) porque, en realidad, estamos creando un nuevo objeto. Pero si copiamos un elemento mutable (como, por ejemplo, una lista) y modificamos el	original, esas	modificaciones se mostrarán	también	en la copia. Igualmente, si	modificamos	la copia, también cambiará el original. Esto ocurre porque, al ser un tipo mutable, no se crea uno nuevo como ocurre con los inmutables y, por tanto, no cambian las referencias y ambos objetos siguen siendo el mismo.""")
print("")

lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
print(lista)
print(id(lista))
copia_de_lista = lista
print(copia_de_lista)
print(id(copia_de_lista))
print("")

copia_de_lista[6] = "Sunday"
print(lista)
print(id(lista))
copia_de_lista = lista
print(copia_de_lista)
print(id(copia_de_lista))
print("")

print("""Si necesitamos copiar una variable con un contenido de tipo mutable, como una lista o un diccionario, debemos hacerlo explícitame""")
print("")

lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
print(lista)
print(id(lista))
print("")

copia_de_lista = list(lista)
print(copia_de_lista)
print(id(copia_de_lista))
print("")

print("Si se cambia un valor en alguna de las listas, no afecta a la otra")
print("")

print(lista)
print(id(lista))
print("")
copia_de_lista[6] = "Sunday"
print(copia_de_lista)
print(id(copia_de_lista))
print("")
