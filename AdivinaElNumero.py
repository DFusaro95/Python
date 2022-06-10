import random

def adivina(x):
    numero_random = random.randint(1,x)
    adivina = 0
    while adivina != numero_random:
        adivina = int(input(f'Adivina el numero entre 1 y {x}: '))
        if adivina > numero_random:
            print('Lo lamento, el numero que elegiste es muy alto')
        elif adivina < numero_random:
            print('Lo lamento, el numero que elegiste es muy bajo')
        
    print(f'Muy bien, has adivinado el numero {numero_random}')

adivina(10)
