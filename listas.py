#!/usr/bin/python
# # -*- coding: utf-8 -*-


print(""" Una lista (también conocidas como vectores o arrays) es una variable que, 
en lugar de contener un valor, contiene una secuencia ordenada de estos, 
a los que se puede acceder por su índice o posición. Se declaran indicando sus elementos, separados por comas, entre corchetes ([]): """)
print("")

lista = ["primero", "segundo", "tercero", "cuarto"]
print(lista)
print("")

print(""" Si es necesario, se puede crear una lista vacía usando unos corchetes sin 
ningún elemento en su interior. """)

lista = []# Esto creará una lista vacía

print(""" Una lista también se puede crear explícitamente, con la función list(): """)

lista = list(("Hola","mundo","palabra"))
print(lista)
print("")

print(""" Para acceder a un elemento de la lista,	ya	sea	para	leerlo	o	para	modificarlo,	es necesario indicar entre corchetes el índice (la posición) de ese elemento, teniendo en cuenta que se comienza a contar desde cero, por lo que el primero es el 0, el segundo es el 1, etc. """)

lista = ["primero", "segundo", "tercero", "cuarto"]
print(lista[2])# Mostrará "tercero"

lista[2] = "Nuevo Elemento"
print(lista[2]) # mostrará "Nuevo Elemento"
print("")

print(""" Para eliminar un elemento de una lista se usa la instrucción del""")
print("")

lista = ["primero", "segundo", "tercero", "cuarto"]
print(lista)
del lista[2]
print(lista)
print("")

print(""" Una lista puede contener datos de todo tipo, lo que incluye cadenas, números y hasta otras listas. Además, dentro de una lista se puede mezclar tipos de datos.
Para acceder al contenido de una lista dentro de otra, se pone un índice a continuación del otro: primero el de la lista inicial, seguido de la lista contenida en esta """)
print("")

lista = [[1, 2, 3], ["a", "b", "c"]]

print(lista[1][0])# Imprimirá "a"
print(lista[0][2])# Imprimirá "3
print("")

lista2=["uno",["one",["hana","du"],"two"],"dos"]

print(lista2[0]) # imprime uno
print(lista2[1][0]) # imprime one
print(lista2[1][1][0]) # imprime hana
print("")
print(lista2[2]) # imprime dos
print(lista2[1][2]) # imprime two
print(lista2[1][1][1]) # imprime du

print("")

print("""se puede acceder a los elementos de la lista desde el ultimo elemenro
hacia el primero usando un numero negativo como indice""")

lista = ["tres", "dos", "uno", "cero"]
print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])
print("")

print("""se puede mostrar solo una parte del la lisra usando (:) para indicar donde inicia hasta donde va""")
print("")

lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(lista)
print("")


print(lista[5:15]) # slicing
# imprime desde la posicion 5 a la posicion 15 menos 1 
print("")

print("""si se omite el primer numero, se mostrara desde el inicio hasta donde se indique, y se se omite el segundo, se mostrara desde donde se indique hasta el final""")
print("")

print(lista[:6]) # imprime desde el 0 hata el 5
print(lista[15:]) # imprime desde el 15 hata el 20
print(lista[:]) # imprime toda la lista
print("")

print("""tambien se puede indicar cada cuanto mostrar los numeros añadiendo
(:)""")
print("")

print(lista[:6:2]) # imprime desde el 0 hata el 5, de dos en dos
print(lista[15::3]) # imprime desde el 15 hata el 20 de tres en tres
print(lista[::5]) # imprime toda la lista de 5 en 5
print("")


mi_lista = list(range(101))
print(mi_lista)
print("")
doble = [i * 2 for i in mi_lista]
print(doble)
print("")
pares = [i for i in mi_lista if i % 2 == 0]
print(pares)
print("")
nones = [i for i in mi_lista if i % 2 != 0]
print(nones)