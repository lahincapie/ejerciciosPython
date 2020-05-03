#!/usr/bin/python
# # -*- coding: utf-8 -*-

print("""Un diccionario es una colaeccion de datos agrupados por clave valor,
donde la calve es el indice puede no solo ser numero si no que puede ser una 
cadena, tuplas o una mezcal entre ellos """)
print("")
print("""al crear un diccionales las partes de clave valor se paran con 
dos puntos (:) y los pares de caleve valor con coma(,) y todo el conjunto 
debe enrradp en llaves ({})""")
print("")

diccionario = {"nombre" : "Alejandra", "ciudad" : "Alberta", "pais" : "Alemania", "cosa": "abrigo", "fruta" : "arandano", "animal" : "alacran", "color" : "azul"}

print(diccionario)
print(type(diccionario))
print("")

print("para acceder a un valor se indica el nombre del diccionario seguido de parentesis cuadrados [] con el indice al que queremos acceder")
print("")

print(diccionario["pais"])
print(diccionario["cosa"])
print(diccionario["fruta"])
print(diccionario["color"])
print("")

print("""los diccionarios se pueden craar explicitamente con la funcion dict(), cambiando los puntos por un signo igual (=) y sin comillas el indice """)
print("")

diccionario2 = dict(nombre = "Laura", 
                    ciudad = "Leticia", 
                    pais = "Libia", 
                    cosa = "lapiz", 
                    fruta = "lulo", 
                    animal = "lombriz", 
                    color = "lila")

print(diccionario2)
print(type(diccionario2))
print("")
print(diccionario2["pais"])
print(diccionario2["cosa"])
print(diccionario2["fruta"])
print(diccionario2["color"])
print("")

print("Un diccionario puede contener cualquier tipo de datos incluidos listas, tuplaa y diccionarios")
print("")

peliculas = {
    "pixar": ("Los increibles", "Toy story", "Monsters Inc", "buscando a Nemo"),
    "disney" : ("Mulan", "El rey leon", "Hercules", "Narnia", "Pinocho")
}

print(peliculas)
print("")
print(peliculas["disney"])
print(peliculas["disney"][0])
print(peliculas["disney"][1])
print(peliculas["disney"][2])
print(peliculas["disney"][3])
print(peliculas["disney"][4])
print(peliculas["disney"][::2])
print("")

kdramas = {
    "Lee Min Ho" : {
        "accion" : "City hunter",
        "escolar" : ("The heirs", "Boy ower flowers"),
        "comedia" : "Personal test",
        "epoca" : ("Faith", "The legend of the blue sea")
    },
    "Park Shin Hye" : {
        "escolar" : ("Hearstrings", "The heirs"),
        "romance" : {
            "juvenil" : "Pinocchio",
            "raro" : ("Flower boy next door", "You're beautiful"),
            "maduro" : "Doctors"
        }
    }
}

print(kdramas)
print(type(kdramas))
print("")

print("Lee Min Ho")
print(kdramas["Lee Min Ho"])
print("Park Shin Hye")
print(kdramas["Park Shin Hye"])
print("")
print(kdramas["Lee Min Ho"]["accion"])
print(kdramas["Lee Min Ho"]["escolar"][0])
print(kdramas["Lee Min Ho"]["escolar"][1])
print(kdramas["Lee Min Ho"]["comedia"])
print(kdramas["Lee Min Ho"]["epoca"][0])
print(kdramas["Lee Min Ho"]["epoca"][1])
print("")
print(kdramas["Park Shin Hye"]["escolar"][0])
print(kdramas["Park Shin Hye"]["escolar"][1])
print(kdramas["Park Shin Hye"]["romance"]["juvenil"])
print(kdramas["Park Shin Hye"]["romance"]["raro"][0])
print(kdramas["Park Shin Hye"]["romance"]["raro"][1])
print(kdramas["Park Shin Hye"]["romance"]["maduro"])