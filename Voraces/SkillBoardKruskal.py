def kruskal(aristas, N):
    aristas.sort(key=lambda item: item[2])
    # conexas = [[i] for i in range(N)]
    # conexas = [set() for i in range(N)]
    conexas = [i for i in range(N)]

    esSol = False
    num = 0
    coste = 0
    while num < len(aristas) and not esSol:
        # Set con los conexos al nodo actual
        nodoIzq = conexas[aristas[num][0]]
        nodoDer = conexas[aristas[num][1]]

        # Si une dos componentes conexas, se unen estas componentes
        if nodoIzq != nodoDer:
            sum = False
            for j in range(N):
                if conexas[j] == nodoDer:
                    conexas[j] = nodoIzq
                    sum = True
            if sum:
                coste += aristas[num][2]

            # Si todas las componentes conexas son iguales, está completo
            allConvex = conexas[0]
            esSol = True
            for i in range(1, N):
                if allConvex != conexas[i]:
                    esSol = False
                    break
        num += 1

    if not esSol:
        # Si no es conexo, uso un nodo Inicial
        coste = 0
        conexaNodo = conexas[0]
        for i in range(N):
            if conexas[i] == conexaNodo:
                for j in range(len(aristas)):
                    if aristas[j][1] == i:
                        coste += aristas[j][2]
                        break
    return coste



nHabilidades, nCaminos = map(int, input().strip().split())

aristas = []
for i in range(nCaminos):
    a, b, z = map(int, input().strip().split())
    aristas.append([a-1, b-1, z])


coste = kruskal(aristas, nHabilidades)
print(coste)