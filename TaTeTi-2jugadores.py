# Variables Necesarias
tablero = ['-', '-', '-',
            '-', '-', '-',
            '-', '-', '-']
jugador1 = 'X'
ganador = None
jugando = True

# Mostrar el tablero de juego
def mostrarTablero(tablero):
    print(tablero[0] + ' | ' + tablero[1] + ' | ' + tablero[2])
    print('----------')
    print(tablero[3] + ' | ' + tablero[4] + ' | ' + tablero[5])
    print('----------')
    print(tablero[6] + ' | ' + tablero[7] + ' | ' + tablero[8])

# Tomar un input de un jugador
def inputJugador1(tablero):
    inp = int(input('Elije un numero entre 1 y 9: '))
    if inp >= 1 and inp <= 9 and tablero[inp-1] == '-': 
            tablero[inp-1] = jugador1
    else:
            print('Lo lamento, El jugador 2 ya tomo esa pocision!')

# Chequear si gana o empata
def lineaHorizontal(tablero):
    global ganador
    if tablero[0] == tablero[1] == tablero[2] and tablero[1] != '-':
        ganador = tablero[0]
        return True
    elif tablero[3] == tablero[4] == tablero[5] and tablero[4] != '-':
        ganador = tablero[3]
        return True
    elif tablero[6] == tablero[7] == tablero[8] and tablero[7] != '-':
        ganador = tablero[6]
        return True

def lineaVertical(tablero):
    global ganador
    if tablero[0] == tablero[3] == tablero[6] and tablero[0] != '-':
        ganador = tablero[0]
        return True
    elif tablero[1] == tablero[4] == tablero[7] and tablero[1] != '-':
        ganador = tablero[1]
        return True
    elif tablero[2] == tablero[5] == tablero[8] and tablero[2] != '-':
        ganador = tablero[2]
        return True

def lineaDiagonal(tablero):
    global ganador
    if tablero[0] == tablero[4] == tablero[8] and tablero[0] != '-':
        ganador = tablero[0]
        return True
    elif tablero[2] == tablero[4] == tablero[6] and tablero[2] != '-':
        ganador = tablero[2]
        return True

def empate(tablero):
    global jugando
    if '-' not in tablero:
        mostrarTablero(tablero)
        print('Juego empatado!')
        jugando = False

# Cambiar de jugador
def cambiarJugador():
    global jugador1
    if jugador1 == 'X':
        jugador1 = 'O'
    else:
        jugador1 = 'X'

def chequearSiGana():
    if lineaHorizontal(tablero) or lineaVertical(tablero) or lineaDiagonal(tablero):
        global jugando
        mostrarTablero(tablero)
        print(f'El ganador es {ganador}')
        jugando = False

# Chequear si gana o empata nuevamente

while jugando:
    mostrarTablero(tablero)
    inputJugador1(tablero)
    chequearSiGana()
    empate(tablero)
    cambiarJugador()