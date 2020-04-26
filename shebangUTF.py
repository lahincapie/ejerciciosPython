#!/usr/local/bin/python3
# # -*- coding: utf-8 -*-

# +++++++++++++++++++++ uso de shebang
# Es posible ejecutar un programa de python sin tener que llamar 
# directamente al interprete de python (osea escribir en la 
# consola python nombreDelArchivo.py). para esto se usa la 
# linea llamada shebang (primera linea) que le indica al sistema 
# operativo que debe de ejecutar el programa.
# los signos "#!" indican que se trata de un script (bloque de de instrucciones)
# y que debe ser leido por el interprete, el texto "usr/bin/python" es la
# ruta donde se encuantra el interprete. en un sistemas UNIX se puede ver la ruta 
# del interprete con which python o para python 3 which python3.
# en windows no es necesario poner esta linea, aunqe no perjudica el codigo,
# windows ignora totalmente cualquier linea de shebang.
# tambien sera necesario modificar los permisos del archivo con el comando 
# chmod +x nombreDelArchivo.py, esto dede la consola ubicada en la carpeta 
# donde esta el archivo. 
# luego para ejecutar el programa solo basta con poner el nombre del archivo
# en la consola, que debe estar unicada en la ruta donde esta nuestro programa
# guardado.

# +++++++++++++++++++++ uso de utf
# payton 2.x espera que el programa este escrito solo con los carateres con los 
# cuenta ASCII, por lo tanto dara error si intentamos usar carateres que no se 
# cuentra en esta codificacion, como es el caso de ñ y las tildes, por esa razon
# se incluye la linea de "# -*- coding: utf-8 -*-", con esta se le indica a
# python que se va a usar la codificacion uthf-8 la cual permite entre otros usar
# tildes y la ñ. en python 3.X esto ya no es necesario


print ('Hola Mundo')
