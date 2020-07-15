def laberinto(tablero, f, c, k, pasosNecesarios):
    if f == len(tablero) - 1 and c == len(tablero) - 1 and pasosNecesarios == k:
        esSol = True
    else:
        esSol = False
        movimientos = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        i = 0
        while not esSol and i < len(movimientos):
            if esFactible(tablero, f + movimientos[i][0], c + movimientos[i][1]):
                tablero[f+movimientos[i][0]][c+movimientos[i][1]] = k
                [tablero, esSol] = laberinto(tablero, f+movimientos[i][0], c+movimientos[i][1], k+1, pasosNecesarios)
                if not esSol:
                    tablero[f + movimientos[i][0]][c + movimientos[i][1]] = 0
            i += 1
    return [tablero, esSol]


def esFactible (tablero, f, c):
    return f >= 0 and f < len(tablero) and c >= 0 and c < len(tablero) and tablero[f][c] == 0



N = int(input())
tablero = []
pasosNecesarios = 0
for n in range(N):
    entrada = input().split()
    for i in range(N):
        entrada[i] = int(entrada[i])
        if entrada[i] == 0:
            pasosNecesarios += 1
    tablero.append(entrada)
paso = 1
pasosNecesarios += 1
tablero[0][0] = paso
[tablero, esSol] = laberinto(tablero, 0, 0, paso+1, pasosNecesarios)
if esSol:
    print("SI")
else:
    print("NO")