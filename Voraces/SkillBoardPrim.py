def prim(nodoInicio, aristas, nNodos):
    aristasCandidatas = []
    solucion = []
    coste = 0
    nodoSig = nodoInicio

    while len(solucion) < nNodos-1:
        # Añadimos a la solucion
        solucion.append(nodoSig)
        for i in range(len(aristas[nodoSig])):
            if aristas[nodoSig][i][0] not in solucion:
                aristasCandidatas.append(aristas[nodoSig][i])

        # Ordenamos para coger la de menor coste
        aristasCandidatas.sort(key=secondValue)
        while len(aristasCandidatas) > 0 and aristasCandidatas[0][0] in solucion:
            aristasCandidatas.pop(0)
        if len(aristasCandidatas) != 0:
            # Actualizamos solucion
            nodoSig = aristasCandidatas[0][0]
            coste += aristasCandidatas[0][1]
            # Sacamos la arista seleccionada
            aristasCandidatas.pop(0)
        else:
            break
    print(coste)


def secondValue(aristasCandidatas):
    return aristasCandidatas[1]


nHabilidades, nCaminos = input().split()
nHabilidades = int(nHabilidades)
nCaminos = int(nCaminos)

aristas = [[] for i in range(nHabilidades)]
for i in range(nCaminos):
    a, b, z = input().split()
    aristas[int(a)-1].append([int(b)-1, int(z)])
    aristas[int(b)-1].append([int(a)-1, int(z)])

prim(0, aristas, nHabilidades)