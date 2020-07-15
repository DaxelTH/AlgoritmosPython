def laberinto(tablero,  f, c, endX, endY, k):
    if f == endX and c == endY:
        esSol = True
    else:
        esSol = False
        movimientos = [[2, 1], [2, -1], [1, 2], [1, -2], [-2, 1], [-2, -1], [-1, 2], [-1, -2]]
        i = 0
        while i < len(movimientos):
            if esFactible(tablero, f + movimientos[i][0], c + movimientos[i][1], k):
                tablero[f+movimientos[i][0]][c+movimientos[i][1]] = k
                [tablero, esSol] = laberinto(tablero, f+movimientos[i][0], c+movimientos[i][1], endX, endY, k+1)
                if not esSol:
                    tablero[f + movimientos[i][0]][c + movimientos[i][1]] = -1
            i += 1
    return [tablero, esSol]


def esFactible (tablero, f, c, k):
    return f >= 0 and f < len(tablero) and c >= 0 and c < len(tablero) and (tablero[f][c] == -1 or tablero[f][c] > k)



N = 5
tablero = []
tablero = [[-1 for x in range(N)] for y in range(N)]
paso = 1
init = input().split()
initX = int(init[0])
initY = int(init[1])
end = input().split()
endX = int(end[0])
endY = int(end[1])
tablero[initX][initY] = paso
# Busqueda solucion mejor
tablero[endX][endY] = 300
[tablero, sol] = laberinto(tablero, initX, initY, endX, endY, paso+1)
print(tablero[endX][endY])