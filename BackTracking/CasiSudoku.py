def sudokuAl(sudoku, casilla, encontrada, sol1):
    if casilla == 81:
        esSol = True
        if encontrada != 1:
            for i in range(9):
                for n in range(9):
                    sol1[i][n] = sudoku[i][n]
            encontrada = 1
            return sudoku, False, encontrada, sol1
        else:
            encontrada = 2
    else:
        esSol = False
        fila = casilla // 9
        columna = casilla % 9
        if sudoku[fila][columna] != 0:
            sudoku, esSol, encontrada, sol1 = sudokuAl(sudoku, casilla+1, encontrada, sol1)
        else:
            # Busco un número factible entre 1 y 9
            i = 1
            while not esSol and i <= 9:
                if esFactible2(sudoku, fila, columna, i):
                    sudoku[fila][columna] = i
                    sudoku, esSol, encontrada, sol1 = sudokuAl(sudoku, casilla+1, encontrada, sol1)
                    if not esSol:
                        sudoku[fila][columna] = 0
                i += 1
    return sudoku, esSol, encontrada, sol1


def esFactible(sudoku, fila, columna, num):
    # Compruebo fila y columna completa
    f = sudoku[:][columna]
    if num in f:
        return False

    c = sudoku[fila][:]
    if num in c:
        return False

    # Compruebo dentro del cuadro de 3x3
    filaIni = 3*(fila // 3)
    filaFin = filaIni + 3
    colIni = 3 * (columna // 3)
    colFin = colIni + 3
    c1 = sudoku[filaIni:filaFin][colIni:colFin]
    if num in c1:
        return False

    return True


def esFactible2(sudoku, fila, columna, num):
    # Compruebo que i no esté en la columna ni el la fila
    for i in range(9):
        if sudoku[i][columna] == num:
            return False
    for i in range(9):
        if sudoku[fila][i] == num:
            return False

    # Compruebo dentro del cuadro de 3x3
    filaIni = 3*(fila // 3)
    filaFin = filaIni + 3
    colIni = 3 * (columna // 3)
    colFin = colIni + 3

    for i in range(filaIni, filaFin):
        for n in range(colIni, colFin):
            if sudoku[i][n] == num:
                return False
    return True


sudoku = [[0 for i in range(9)] for n in range(9)]

for i in range(9):
    fila = list(map(int, input().split()))
    for n in range(len(fila)):
        sudoku[i][n] = fila[n]

sol1 = [[0 for i in range(9)] for n in range(9)]
[sudoku, esSol, encontrada, sol1] = sudokuAl(sudoku, 0, 0, sol1)

if encontrada == 2:
    print("casi sudoku")
elif encontrada == 1:
    for i in range(9):
        for n in range(9):
            print(sol1[i][n], "", end="")
        print()
else:
    print("imposible")

