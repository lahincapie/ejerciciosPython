#usr/bin/python
# -*- coding: utf-8 -*-

print("""
Una función no es más que un bloque de código que se puede usar varias veces 
en varios puntos distintos de nuestro programa. Nos evita tener que repetir 
código y facilita la lectura y el mantenimiento del programa.
Para declarar una función usamos la palabra reservada def seguida del nombre 
de la función, un paréntesis (del que luego hablaremos) y dos puntos. A 
continuación de esto, e indentado un nivel, se encuentra el código en sí 
de la función.
Los nombres de las funciones siguen las mismas reglas que los nombres de las 
variables (deben comenzar por una letra o guión bajo, no pueden contener 
espacios ni pueden comenzar por un número, pero sí contener números). Se 
recomienda usar nombres en minúsculas y, si constan de más de una palabra, 
estas deberían estar separadas por guiones bajos.
""")
print("")

def saludo():
    print("Hola python")

print("""
Este ejemplo, tal como está, no hace nada: una función debe ser invocada para 
que se ejecute. Para invocar a la función se usa su nombre seguido de un 
paréntesis. Cada vez que se llama de este modo a la función, se ejecuta su código.
""")
print("")

saludo()

print("")
print("A una función que no retorna nada se la denomina, tradicionalmente, subrutina")
print("")
print("una función puede retornar un resultado usando la orden return")
print("")

def dame_pi(): 
    numero_pi = 3.14159 
    return numero_pi
    
pi = dame_pi()
print(pi)
print("")
print(dame_pi())
print("")

def saluda(): 
    return "hola", "mundo"

hola = saluda()# hola contiene una tupla de dos elementos
print(hola)

print("")

print("""
Sin duda, lo que da realmente utilidad a las funciones es la capacidad de 
recibir parámetros o argumentos. Un argumento o parámetro es un valor que 
se le pasa a la función y que esta puede usar como variable para operar 
con él.Los	parámetros	que	puede	recibir	una	función	deben	asignarse	
al	definir	esta, situándolos entre los signos de paréntesis. Ese nombre 
actúa como una variable interna a la función.
Del mismo modo, al llamar a la función, se le debe pasar el valor que 
tendrá esa variable (el argumento) en el paréntesis """)
print("")

def cuadrado(numero): 
    cuadrado = numero * numero 
    return cuadrado

resultado = cuadrado(5)
print(resultado)
print("")

print(""" Una	función	puede aceptar más de un	argumento. Para ello, al definirla,	
se	enumeran por orden, separándolos por comas. Al llamar a la función, 
los argumentos deben pasarse en el mismo orden en el que se	han	definido. """)

def saluda(nombre, sexo): 
    print("Hola " + nombre) 
    if sexo == "M" or sexo == "m": 
        print("¿Cómo te va, hombre?") 
    elif sexo == "F" or sexo == "f": 
        print("¿Cómo te va, mujer?") 
    else: print("¿Cómo te va?")
    
saluda("Ale", "F")

print("")
print(""" 
Se puede dar un valor por defecto a un parámetro en	la	definición	de	la	función. 
Para hacerlo solo hay que asignárselo usando el signo igual “=” tras el nombre del 
parámetro. Si al llamar a la función no se le pasa ese argumento,	se	usará	el	
valor	por	defecto	predefinido.	De	este	modo,	ese	argumento	es opcional, 
y el intérprete de Python no dará un error si no se le pasa un valor al llamar a la 
función.
""")
print("")
def tabla_multiplicar(nombre, numero = 1): 
    print("Tabla de multiplicar del " + str(numero)) 
    print("Impresa automáticamente por " + nombre) 
    
    i = 0 
    
    while i < 11: 
        print(str(numero) + " X " + str(i) + " = " + str(numero * i))
        i += 1

tabla_multiplicar("Ale", 8)

print("""
Como los valores de los parámetros se asignan a estos por orden, si en una 
función hay parámetros con valor por defecto junto con otros que no lo tienen, 
deben ponerse por orden: primero los que no tienen valor por defecto (y, por 
tanto, son obligatorios) y luego los que sí lo tienen (y son opcionales)
""")
print("")
print(""" 
A veces tenemos funciones de las que no sabemos cuántos argumentos van a recibir. 
Cuando queremos que una función acepte un número arbitrario de argumentos usamos 
los llamados args. Un arg no es más que un parámetro que se	define	como	
cualquier otro, pero con un asterisco delante del nombre. Python interpreta eso, 
en lugar de una variable, como una lista en la que se almacenarán todos los 
argumentos que se reciba
""")
print("")

def imprime_lista(nombre_lista, *cosas): 
    print("Lista de " + nombre_lista) 
    
    for cosa in cosas: 
        print (cosa)
        
imprime_lista("Piezas", "tornillo", "tuerca", "otro torni-llo", "cable")


print(""" Si una función debe aceptar	argumentos	fijos	junto	con	args, los argumentos fijos deben ponerse antes que los args ya que, al ser una lista, estos últimos “capturarían”	todos	los	valores	y	los	fijos	no	llegarían	a	tener	ningún	valor.

Un	refinamiento	a	esto	son	los	**kwargs (keyword arguments). Se trata de argumentos que pasan pares de clave-valor, y se reciben como un diccionario """)
print("")

def imprime_datos(nombre, **datos):
    print("Datos de " + nombre) 
    for clave in datos: 
        print(clave + ": " + datos[clave])

imprime_datos("Pablo", edad = "mucha", estado = "enloqueci-do", guapo = "no")