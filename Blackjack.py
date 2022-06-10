# Variables necesarias
import random
mazo = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q', 'A', 'J', 'K', 'Q', 'A', 'J', 'K', 'Q', 'A', 'J', 'K', 'Q', 'A']
manoDelJugador = []
manoDelRepartidor = []
jugadorIn = True
repartidorIn = True

# Repartir las cartas
def repartirCarta(turno):
    carta = random.choice(mazo)
    turno.append(carta)
    mazo.remove(carta)

# Clacular el total de cada mano
def total(turno):
    total = 0
    negras = ['J', 'K', 'Q']
    for carta in turno:
        if carta in range(1,11):
            total += carta
        elif carta in negras:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total

# Chequear por un ganador
def mostrarManoRepartidor():
    if len(manoDelRepartidor) == 2:
        return manoDelRepartidor[0]
    elif len(manoDelRepartidor) > 2:
        return manoDelRepartidor[0], manoDelRepartidor[1]

# Loop del juego
for _ in range(2):
    repartirCarta(manoDelRepartidor)
    repartirCarta(manoDelJugador)

while jugadorIn or repartidorIn:
    print(f'El repartidor tiene {mostrarManoRepartidor()} y X')
    print(f'Tu tienes {manoDelJugador} por un total de {total(manoDelJugador)}')
    if jugadorIn:
        stayOrHit = input('1: Stay\n2: Hit\n')
    if total(manoDelRepartidor) > 16:
        repartidorIn = False
    else:
        repartirCarta(manoDelRepartidor)
    if stayOrHit == '1':
        jugadorIn = False
    else:
        repartirCarta(manoDelJugador)
    if total(manoDelJugador) >= 21:
        break
    elif total(manoDelRepartidor) >= 21:
        break

if total(manoDelJugador) == 21:
    print(f'\nTienes {manoDelJugador} por un total de {total(manoDelJugador)} y el repartidor tiene {manoDelRepartidor} por un total de {total(manoDelRepartidor)}')
    print('BlackJack!! Tu ganas')
elif total(manoDelRepartidor) == 21:
    print(f'\nTienes {manoDelJugador} por un total de {total(manoDelJugador)} y el repartidor tiene {manoDelRepartidor} por un total de {total(manoDelRepartidor)}')
    print('Blackjack!! El repartidor gana')
elif total(manoDelJugador) > 21:
    print(f'\nTienes {manoDelJugador} por un total de {total(manoDelJugador)} y el repartidor tiene {manoDelRepartidor} por un total de {total(manoDelRepartidor)}')
    print('Te has pasado!! El repartidor gana')
elif total(manoDelRepartidor) > 21:
    print(f'\nTienes {manoDelJugador} por un total de {total(manoDelJugador)} y el repartidor tiene {manoDelRepartidor} por un total de {total(manoDelRepartidor)}')
    print('El repartidor se ha pasado!! Tu ganas')
elif 21 - total(manoDelRepartidor) < 21 - total(manoDelJugador):
    print(f'\nTienes {manoDelJugador} por un total de {total(manoDelJugador)} y el repartidor tiene {manoDelRepartidor} por un total de {total(manoDelRepartidor)}')
    print('El repartidor gana!')
elif 21 - total(manoDelJugador) < 21 - total(manoDelRepartidor):
    print(f'\nTienes {manoDelJugador} por un total de {total(manoDelJugador)} y el repartidor tiene {manoDelRepartidor} por un total de {total(manoDelRepartidor)}')
    print('Tu ganas!')