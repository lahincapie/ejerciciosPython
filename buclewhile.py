#usr/bin/pyhon
#  -*- coding: utf-8 -*-

print(""" Un bucle (ciclo, loop) es un bloque de código que se ejecuta repetidas veces mientras se cumpla una condición determinada. La instrucción while crea un bucle que se ejecutará mientras su condición sea cierta. Cuando la condición deje de ser cierta el curso del programa continuará normalmente. Si la condición es falsa desde el principio, ese bloque no se ejecutará ni una sola vez.""")
print("")

a = 0

while a < 10: 
    a = a + 1 
    print(a, end = " // " )


print("")

a = 10

while a < 10: 
    a = a + 1 
    print(a)

print("")

print("""While también permite una sentencia else que se ejecutará cuando la condición del bucle no sea cierta (es decir, fuera del bucle) """)
print("")


a = 10

while a < 10: 
    a = a + 1 
    print(a, end = " // " )
else:
    print("no se cumplio la condicion")

print("")
print("""En un buclewhile también se puede usar la instrucción break, que corta el flujo del bucle en ese punto y continúa la ejecución del script por la primera instrucción posterior al bucle. Si hubiese una cláusula else, esta tampoco se ejecutaría """)

a = 10

while a < 10:
    a = a + 1
    if a == 3:
        break
    print(a)

print("")

print("En este ejemplo hemos puesto un if anidado dentro del while que, cuando la variable “a” vale 3, provoca un break. Aunque el bucle está diseñado para llegar hasta 10, el break detiene el bucle y la variable nunca se incrementa hasta ese valor.Una opción parecida es continue, que también interrumpe el bucle pero solo en el ciclo en el que se ejecuta, volviendo al principio del bloque ")
print("")

a = 0

while a < 10:
    a = a + 1
    if a == 3:
        continue
    print(a)

print("")
print("""En este ejemplo, que solo se diferencia del anterior por haber cambiado el break por un continue, el bucle se recorre entero imprimiendo los números del uno al diez, pero se omite el tres porque la orden continue evita que llegue a ejecutarse el print. """) 
print("")

print("Se puede anidar bucles dentro de otros para conseguir resultados mas complejos.")
print("")
a = 1

while a <= 10:
    b = 1
    while b <= 10:
        print("{} * {} = ".format(a,b) + str(a*b))
        b = b + 1
    print("")
    a = a + 1


#ejemplo de raiz cuadrada

objetivo = 4
respuesta = 0 

while respuesta ** 2 < objetivo:
    respuesta += 1
if respuesta ** 2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tiene una raiz cuadrada exacta')