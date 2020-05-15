# -*- coding: utf-8 -*-
def binary_search(numeros, numero_a_encontrar, low, high):
    if low > high:
	    return False

    mid = int((low+high) / 2)
    
    if numeros[mid] == numero_a_encontrar:
        return True
    elif numeros[mid] > numero_a_encontrar:
        return binary_search(numeros, numero_a_encontrar, low, high - 1)
    else: 
        return binary_search(numeros, numero_a_encontrar, mid + 1, high)


if __name__ == '__main__':
	numeros = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]
	#numeros = [1, 3, 5, 7, 9, 10, 12, 13, 15, 16, 17, 18, 20, 21, 22, 25, 26, 34, 36, 49, 51]

	numero_a_encontrar = int(input("Ingrese numero:  "))

	resultado = binary_search(numeros, numero_a_encontrar, 0, len(numeros) -1)

	if resultado is True:
		print('El numero si esta en la lista ')
	else:
		print('El numero no esta en la lista ')