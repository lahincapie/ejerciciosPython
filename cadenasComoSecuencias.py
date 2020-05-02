#usr/bin/python
# -*- coding: utf-8 -*-

print("""En python las cadenas de texto pueden ser tratadas como tuplas, 
esto significa que se puede acceder a cada posicion de la cadena   """)
print("")

cadena_de_texto = "Esto es una cadena de texto que puede contener numeros, letras o signos, como 1 0 2 0 () o %"

print(cadena_de_texto)
print(type(cadena_de_texto))
print("")

print(cadena_de_texto[3]) 
print(cadena_de_texto[10:26]) 
print(cadena_de_texto[:30]) 
print(cadena_de_texto[30:]) 
print(cadena_de_texto[::2]) 
print("")

print(""" Al igual que en el caso de las tuplas, las cadenas son inmutables, 
y el slicing se puede usar solo para leer y no para introducir caracteres, por 
lo que no se puede modificar la cadena. """)