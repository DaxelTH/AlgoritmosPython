sudoku = {}
sudoku['fila'] = []
sudoku['columna'] = [[] for i in range(9)]
for i in range(9):
    sudoku['fila'].append(list(map(int, input().split())))
    for n in range(9):
        sudoku['columna'][n].append(sudoku['fila'][i][n])

print(sudoku)
