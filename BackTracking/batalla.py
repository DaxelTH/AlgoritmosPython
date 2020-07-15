def nReinasVA(tablero, fila):
    if fila == len(tablero):
        esSol = True
    else:
        esSol = False
        col = 0
        while not esSol and col < len(tablero):
            if EsFactible(tablero, fila, col):
                tablero[fila][col] = 1
                [tablero, esSol] = nReinasVA(tablero, fila+1)
                if not esSol:
                    tablero[fila][col] = 0
            col += 1
    return [tablero, esSol]


def EsFactible (tablero, f, c):
    colOk = True
    indF = f
    indC = c
    while colOk and indF >= 0:
        if tablero[indF][indC] == 1:
            colOk = False
        indF -= 1
    if not colOk:
        return False
    diag1Ok = True
    indF = f-1
    indC = c-1
    while diag1Ok and indF >= 0 and indC >= 0:
        if tablero[indF][indC] == 1:
            diag1Ok = False
        indF -= 1
        indC -= 1
    if not diag1Ok:
        return False
    diag2Ok = True
    indF = f-1
    indC = c+1
    while diag2Ok and indF >= 0 and indC < len(tablero):
        if tablero[indF][indC] == 1:
            diag2Ok = False
        indF -= 1
        indC += 1
    if not diag2Ok:
        return False
    else:
        return True


fila = input().split()
numFilas = int(fila[0])
numPlayers = int(fila[1])
tablero = [[0 for x in range(numFilas)] for y in range(numFilas)]
if numPlayers > 0:
    players = input().split()
    for n in range(numPlayers):
        ind = int(players[n])
        tablero[n][ind] = 1
else:
    numPlayers = 0
[tablero, esSol] = nReinasVA(tablero, numPlayers)
if esSol:
    print("ADELANTE")
else:
    print("VUELVE A EMPEZAR")
