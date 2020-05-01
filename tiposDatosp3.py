#!usr/bin/python
# -*-coding: utf-8 -*-

# Algunos tipos de datos que python tiene predefinidos son:



print("")
#____________________________________________________________________
print("____________________________________________________________")
print("____________________________________________________________")
#____________________________________________________________________
print("")

print("-----------------------Enteros (int)-----------------------")
print("Los enteros son números sin decimales, positivos o negativos")
print("")


numero_minimo_en32_bits = -2147483647
numero_maximo_en32_bits = 2147483647
numero_minimo_en64_bits = -9223372036854775807
numero_maximo_en64_bits = 9223372036854775807

print("Número minimo en computadores de 32 bits: ")
print(numero_minimo_en32_bits)
print("")
print("Número maximo en computadores de 64 bits: ")
print(numero_maximo_en32_bits)
print("")
print("Numero minimo en computadores de 64 bits: ")
print(numero_minimo_en64_bits)
print("")
print("Número maximo en computadores de 64 bits: ")
print(numero_maximo_en64_bits)



print("")
#____________________________________________________________________
print("____________________________________________________________")
print("____________________________________________________________")
#____________________________________________________________________
print("")

print("--------------------Enteros Largos (long)--------------------")
print("Los enteros son números sin decimales, positivos o negativos, \npero en este caso no tienen limite superior ni inferior pero un numero \n(5, por ejemplo) ocupa mucho mas espacio en memoria cuando se guardo como tipo de dato \nlong que cuando se guarda como tipo de dato int ") # \n produce salto de linea
print("Para indicar que es un entero largo se usa 'L' al final del numero, \nesto para python 2, en python 3 los numero no tienen limitaciones de tamaño")
print("")

entero_larago = 290420201022

print(entero_larago)

print("")
#____________________________________________________________________
print("____________________________________________________________")
print("____________________________________________________________")
#____________________________________________________________________
print("")

print("------------------Números Flotantes (float)------------------")
print("")
print("Son los numero decimales, estos se separan con un pnto (.)")
print("")


print("maximo flotante que permite para un flotante es")
print("1.7976931348623157e+308")
print("")
print("minimo flotante que permite para un entero largo es")
print("2.2250738585072014e-308.")


print("")
#____________________________________________________________________
print("____________________________________________________________")
print("____________________________________________________________")
#____________________________________________________________________
print("")

print("----------------------Números complejos----------------------")
print("")
print("Son una abstraccion matematica que idealmente se una para resolver problemas con raices de numeros negativos")
print("")

numero_complejo = 56 + 3j

print(numero_complejo)

print("")
#____________________________________________________________________
print("____________________________________________________________")
print("____________________________________________________________")
#____________________________________________________________________
print("")

print("-------------------------Notaciones-------------------------")
print("")


print("Base 8")
octal = 0o10
print("10 = ", end="")
print(octal)
print("8 = " + format(8, 'o'))


print("")
#____________________________________________________________________
print("____________________________________________________________")
#____________________________________________________________________
print("")

print("Base 2")
binario = 0b11
print("11 = ", end ="")
print(binario)
print("3 = " + format(3, 'b'))


print("")
#____________________________________________________________________
print("____________________________________________________________")
#____________________________________________________________________
print("")

print("Base 16")
hexadecimal = 0xB16A
print("B16A = ", end ="")
print(hexadecimal)
print("45418 = " + format(45418, 'x'))
print("")


print("")
#____________________________________________________________________
print("____________________________________________________________")
print("____________________________________________________________")
#____________________________________________________________________
print("")

print("-------------------------Booleanos-------------------------")
print("")

print("Los bolleanos sirven para mostrar los valores logicos de \nfalso (false) y verdadero (true)")

print("Valor verdadero es: True")
print("Valor falso es: False")


print("")
#____________________________________________________________________
print("____________________________________________________________")
print("____________________________________________________________")
#____________________________________________________________________
print("")

print("-------------------------Cadenas-------------------------")
print("")


print("Una cadena es un grupo de caracteres que seran tratados como texto \ny que estan dentro de comillas simples o dlobles")

esto_es_una_cadena = "Hola Mundo"
esto_tambien_es_una_cadena = 'Hola de nuevo'

esto_es_una_cadena_en_varias_lineas = '''primera linea
segunda linea
tercera linea
 '''

print(esto_es_una_cadena_en_varias_lineas)

cadena_con_comillas = "Si se quiere usar comillas dentro de una cadena \nse deben usar comillas distintas: \nsi se uso comillas dobles para encerrar la cadenas, \ndentro se deben usar las comillas simples ('') dentro de la cadena"

print(cadena_con_comillas)
print("")

cadena_con_comillas = ("Tambien se puede anteponer barra invertida para \nque python no interprete el \" signo de comillas\" ")

print(cadena_con_comillas)
print("")

print("La barra invertida se usa para 'escapar' algun \ncaracter que tenga un significado especial para python")
print("")

print("algunas combinaciones con barra invertida tienen significado espcial en python")

print(""" 
        \    Barra invertida (\)
        \\'  Comilla simple (‘)
        \\"  Comilla doble (“)
        \\a  Campana (BEL)
        \\b  Retroceso (BS)
        \\f  Salto de página (FF)
        \\n  Nueva línea (LF)
        \\r  Retorno de carro (CR)
        \\t  Tabulador (TAB)
        \\v  Tabulador vertical Tab (VT)
        
 """)

cadena_raw = r"los signos como \n y \t se muestran tal como estan sntponiendo r al inicio de la cadena"

print(cadena_raw)

print("")
#____________________________________________________________________
print("____________________________________________________________")
print("____________________________________________________________")
#____________________________________________________________________
print("")

print("-------------------------None-------------------------")
print("")


print(""" Un tipo especial de Python es None, que indica la ausencia de valor. 
No es lo mismo una variable que contiene una cadena vacía ("") o el número cero, 
que una variable que no contiene ningún valor. 
None se usa para representar esa ausencia de valor. """)


print("")
#____________________________________________________________________
print("____________________________________________________________")
print("____________________________________________________________")
#____________________________________________________________________
print("")

print("----------------------ver tipo de datos----------------------")
print("")


print(""" 
Para saber el tipo de dato de una variable o de un literal
se usa la funcion type()
""")

texto = "Hola Mundo"
entero = 21
verdad = True
falso = False
vacio = " "
cadena_vacia = "" 

print(type(texto)) # Tipo str
print(type ("Hola")) # Tipo str
print(type (14.5)) # Tipo float
print(type (entero)) # Tipo int
print(type (18)) # Tipo long
print(type (34 +  56j)) #complex
print(type(verdad)) # bool
print(type(falso)) #bool
print(type(vacio)) #str
print(type(cadena_vacia)) #str


print("")
#____________________________________________________________________
print("____________________________________________________________")
print("____________________________________________________________")
#____________________________________________________________________
print("")

print("------------------Manipular tipos de datos------------------")
print("")


print("Python dispone de algunas funciones que nos pueden \nservir para transformar datos de un tipo a otro. \nla función int(numero) toma un número (o una cadena que \ncontenga un número) y retorna un entero")
print("")

texto = "10"
decimal = 21.15
un_entero = int(texto)

print(type(texto))
print(type(decimal))
print(type(un_entero))
print(type(int(decimal)))

print("")

print("Para convertir un número en otro en coma flotante, se usa la función float(numero)")
print("")

flotante = float(4)

print(flotante) 
print(type(flotante))

print("")

print("para obtener una cadena a partir de otros valores, tenemos la función str(x)")
print("")

entero = 5
decimal = 21.15


cadena_entero = str(entero)
cadena_decimal = str(decimal)

print(type(cadena_entero))
print(type(cadena_decimal))
print("")

"""print("Entero, hexadecimal, osctal")

 entero = 500
hexadecimal = hex(entero)
octal = oct(entero)

print(hexadecimal)
print(octa) """

