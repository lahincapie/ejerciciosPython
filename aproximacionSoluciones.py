#usr/bin/python
# -*- coding: utf-8 -*-

import time

objetivo = int(input('Escoge un numero: ')) # Pide un numero al usauario
epsilon = 0.01 # que tan cerca queremos llegar de la respuesta
paso = epsilon**2 # que tanto se va acercando a la respuesta 
respuesta = 0.0 # guarda la respuesta al final de la iteracion 
contador = 0
tiempo = time.time()

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print((respuesta**2 - objetivo), epsilon, contador)
    respuesta += paso
    contador += 1

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada de {objetivo}')
    print(f'Fueron {contador} iteraciones')
    print(f'Fueron {tiempo} segundos')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    print(f'Fueron {contador} iteraciones')
    print(f'Fueron {tiempo} segundos')