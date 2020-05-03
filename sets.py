#!/usr/bin/python
# # -*- coding: utf-8 -*-


print("""Un set o conjunto es una colección no ordenada de objetos. No posee un índice como las listas o los diccionarios, y no puede contener objetos repetidos. Se declara usando llaves ({}) como un diccionario pero, dado que no tiene pares clave-valor, simplemente se separan sus elementos por comas. Un set también puede declararse explícitamente usando la función set().""")
print("")
print("""No se puede crear un set vacío usando llaves porque se crearía un diccionario. Para crearlo es necesario hacerlo explícitamente, simplemente con conjunto = set(). Un set no puede contener valores mutables""")
print("")

cubiertos = {"tenedor","cuchara","cuchillo", "cucharilla"}
vajilla = set(["plato","taza","copa"])

print(cubiertos)
print(vajilla)