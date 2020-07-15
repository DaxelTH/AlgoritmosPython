def dijkstraCaminosMinimosDesdeUnNodo(posInicial, numNodos, aristas):
    visitados = set()
    posActual = posInicial

    vectorDist = [float("inf")] * numNodos
    visitados.add(posActual)
    vectorDist[posActual] = 0

    while len(visitados) != numNodos:
        min = float("inf")
        nodoSig = -1
        for i in range(len(aristas[posActual])):
            if not visitados.__contains__(aristas[posActual][i][0]):
                if vectorDist[aristas[posActual][i][0]] > vectorDist[posActual] + aristas[posActual][i][1]:
                    vectorDist[aristas[posActual][i][0]] = vectorDist[posActual] + aristas[posActual][i][1]

        for i in range(len(vectorDist)):
            if not visitados.__contains__(i) and min > vectorDist[i]:
                min = vectorDist[i]
                nodoSig = i

        if nodoSig != posActual:
            visitados.add(nodoSig)
            posActual = nodoSig

    return vectorDist


def secondValue(aristasCandidatas):
    return aristasCandidatas[1]


N, M, T = map(int, input().strip().split())
aristas = [[] for i in range(N)]
for i in range(M):
    a, b, z = map(int, input().strip().split())
    aristas[a].append([b, z])
    aristas[b].append([a, z])

vectorDistancias = dijkstraCaminosMinimosDesdeUnNodo(0, N, aristas)
maximo = sum(vectorDistancias)
if maximo <= T:
    print(maximo)
else:
    print("Somos un fraude")