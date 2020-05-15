objetivo = int(input('Escribe un numero: '))
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

