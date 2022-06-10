# ORGANIZACION
#Crear una variable de los caracteres a utilizar
#Colocar los inputs
#Utilizar RANDOM para seleccionar al azar
#Ordenar todo en un bucle

import random

print ('Bienvenidos al Generador de Contraseñas')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&-.,@0123456789'

number = input('Cantidad de contraseñas a generar: ')
number = int(number)

length = input('Cantidad de caracteres: ')
length = int(length)

print('\nAqui estan tus contraseñas: ')

for contraseña in range (number):
    password = ''
    for c in range (length):
        password += random.choice(chars)
    print(password)
