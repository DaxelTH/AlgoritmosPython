def prim(nodoInicio, aristas, nNodos):
    aristasCandidatas = []
    solucion = []
    coste = 0
    nodoSig = nodoInicio
    nodoAnterior = -1
    pesosAcumNodos = [[0] for i in range(nHabitaciones)]
    while len(solucion) < nNodos - 1:
        # Añadimos a la solucion
        solucion.append(nodoSig)
        for i in range(len(aristas[nodoSig])):
            if aristas[nodoSig][i][1] not in solucion:
                aristasCandidatas.append(aristas[nodoSig][i])

        # Ordenamos para coger la de menor coste
        aristasCandidatas.sort(key=thirdValue)
        while len(aristasCandidatas) > 0 and aristasCandidatas[0][1] in solucion:
            aristasCandidatas.pop(0)
        if len(aristasCandidatas) != 0:
            # Actualizamos nodos
            nodoAnterior = aristasCandidatas[0][0]
            nodoSig = aristasCandidatas[0][1]

            # Sacamos la arista seleccionada
            aristasCandidatas.pop(0)
        else:
            break
    print(pesosAcumNodos)


def thirdValue(aristasCandidatas):
    return aristasCandidatas[2]


nHabitaciones, nPuertas, tMax = input().split()
nHabitaciones = int(nHabitaciones)
nPuertas = int(nPuertas)
tMax = int(tMax)

aristas = [[] for i in range(nHabitaciones)]
for i in range(nPuertas):
    a, b, z = input().split()
    aristas[int(a)].append([int(a), int(b), int(z)])
    aristas[int(b)].append([int(b), int(a), int(z)])

prim(0, aristas, nHabitaciones)