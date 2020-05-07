#usr/bin/python
# -*- coding: utf -*-

print(""" Lo que hace try es ejecutar un bloque de sentencias en un “entorno controlado”, para que el error generado (si se da) no detenga el programa, sino que se retorne de modo que pueda manejarse. 

Por ejemplo, el clasico error de la division por 0 hara que el programa falle y se detenga en ese punto. sin embargo con el uso de try podemos evitar la interrupcion del programa """)
print("")

dividendo = 1
divisor = 0

try: 
    resultado = dividendo/divisor 
    print("La división resulta: ", resultado)
except: 
    if divisor == 0: 
        print("No puedes dividir por cero")

print("Hemos terminado")


print("")
print("""python tiene una forma mas concreta de manejar los errores usando el o los tipos de error que se quieran manejar  """)
print("")

dividendo = "A"
divisor = 2

try: 
    resultado = dividendo/divisor 
    print("La división resulta: ", resultado)
except ZeroDivisionError: 
    if divisor == 0: 
        print("No puedes dividir por cero") 
except TypeError: 
    print("Hay que ser bruto: eso no es un número")

print("")
print("Cada uno de los bloques except se ejecuta solo si se da el tipo de error especificad")
print("")

dividendo = 1
divisor = 2
try: 
    resultado = dividendo/divisor
except ZeroDivisionError: 
    if divisor == 0: 
        print("No puedes dividir por cero, animal")
except TypeError: 
    print("Hay que ser bruto: eso no es un número")
else: 
    print("La división resulta: ", resultado)



print("")
print("Es importante hacer notar que dentro del try hemos dejado solo la instrucción que	requiere	que	verifiquemos,	dejando	el	print en el else final")