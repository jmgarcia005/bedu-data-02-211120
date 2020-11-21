# Script que calcula la tabla de multiplicar de un número

#Solicitar numero al ususario por consola
numero = input('¿Qué número quieres multiplicar?')
#el dato a ingresar por el ususario es una cadena 'str'
#se debe convertir a numero para multiplicar
numero = int(numero)

for n in range (10):
    r = numero * (n + 1)
    print(f'A continuación se presenta la tabla del {numero}')

    #A contunación se muestra la tabla del número NNN
    #-------------------------
    #8 * 1 = 8
    #8 * 2 = 16
    #8 * 3 = 24
