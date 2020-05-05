#usr/bin/python
# -*- coding: utf-8 -*-

print ("""La	estructura	básica	para	el	control	del	flujo	de	un	programa	es	el	“si	condicional” if, que permite la ejecución de un segmento de código dependiendo de las condiciones concretas y""")
numero = 2

if numero > 20:
    print("El numero es mayor a 20")
    print("estamos aqui :)")

print("sea el numero mayor o menor a 20 siempre se impime esto")
print("")

print("""En python no se puede dejar una instruccion vacia, ya que esto genera un error (IndentationError: expected an indented block), si es necerio dejar la instruccion vacia, se puede usar la orden pass que no tienen efecto ninguno en el codigo pero permite que continue sin generar error """)
print("")

if numero < 20:
    pass

print("la orden pass simplemente no hace nada")
print("")


print("para completar la estructura condicional se unsa el else, que ejecuta las intrucciones si no se cumple el condicional if")
print("")

numero = 2

if numero > 20:
    print("El numero es mayor a 20")
    print("aqui se cumple el condicional if :)")
else:
    print("El numero es nenor a 20")
    print("esta es la parte del else, el condicional if no se cumplio")

print("")
print("""Se se requiere validar mas de una condicion se usa elif, que es la contraccion de else if, para anidar mas instrucciones """)
print("")

variable = 3

if variable > 3: 
    print ("La variable es mayor que tres") 
    print ("aqui estamos en la condicional if")
elif variable < 3: 
    print ("La variable es menor que tres") 
    print ("Esta el la condicional elif")
else: 
    print ("La variable es tres") 
    print ("este es el else")
            
