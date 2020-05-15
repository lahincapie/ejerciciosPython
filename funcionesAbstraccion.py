#usr/bin/python
# -*- coding: utf-8 -*-


"""
Dado un numero se dara como respuesta la raiz cuadrada de este,
utilizando el metodo indicado por el usuario
"""

opcion = False


def enumeracion_exhaustiva(objetivo):
"""
Enumeracion exhaustiva:
va buscando paso a paso la posible solucion del problema, 
en esta caso prueba todos los numeros en busca de la raiz
cuadrada del numero ingresado
"""

    respuesta = 0
    while respuesta ** 2 < objetivo:
        respuesta += 1
    if respuesta ** 2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')


"""
Aproximacion de soluciones:
Busca la raiz cuadrada del numero dado a partir de una aproximacion 
"""

def aproximacionSoluciones(numero):
    epsilon = 0.01 # que tan cerca queremos llegar de la respuesta
    paso = epsilon**2 # que tanto se va acercando a la respuesta 
    respuesta = 0.0 # guarda la respuesta al final de la iteracion 
    contador = 0
    
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), epsilon, contador)
        respuesta += paso
        contador += 1

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada de {objetivo}')
        print(f'Fueron {contador} iteraciones')
        
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
        print(f'Fueron {contador} iteraciones')
        

"""
Busqueda binaria:
Divide en dos el rango de posibles respuestas y busca en el rango
que cumple con la condicion dada, solo funciona para elementos ordenados
"""

def busquedaBinaria(numero):
    epsilon = 0.00000001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2
    contador = 1

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'{contador} ||| bajo = {bajo} ||| alto = {alto} ||| respuesta = {respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2
        contador += 1

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')



objetivo = (int(input('escribe un numero: ')))

print('')
print('Enumeracion exhaustiva: = 1')
print('Aproximacion de soluciones: 2')
print('Busqueda binaria: = 3')
print('')


while opcion == False:
    solucion = (int(input('Elija una opcion: ')))

    if solucion < 1 or solucion > 3:
        print('Opcion no valida')
        opcion = False
    elif solucion == 1:
        enumeracionExhaustiva(objetivo)
        opcion = True
    elif solucion == 2:
        aproximacionSoluciones(objetivo)
        opcion = True
    else:
        busquedaBinaria(objetivo)
        opcion = True


