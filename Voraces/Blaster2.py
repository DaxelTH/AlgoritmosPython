def dijkstra(posInicial, posObjetivo, potencia, pesosNodos, numNodos, aristas):
    visitados = []
    posActual = posInicial
    visitados.append(posActual)
    vectorDist = [float("inf")] * numNodos
    fin = False
    while posActual != posObjetivo and potencia >= 0:
        min = float("inf")
        nodoSig = -1
        for i in range(len(aristas[posActual])):
            if not visitados.__contains__(aristas[posActual][i]):
                if posObjetivo == aristas[posActual][i]:
                    fin = True
                    break
                else:
                    if vectorDist[aristas[posActual][i]] != float("inf"):
                        vectorDist[aristas[posActual][i]] += pesosNodos[aristas[posActual][i]]
                    else:
                        vectorDist[aristas[posActual][i]] = pesosNodos[aristas[posActual][i]]
                    if min > vectorDist[aristas[posActual][i]]:
                        min = vectorDist[aristas[posActual][i]]
                        nodoSig = aristas[posActual][i]
        if fin:
            return potencia
        if nodoSig != posActual:
            posActual = nodoSig
            potencia -= min
            visitados.append(posActual)
        else:
            potencia = 0
        print(vectorDist)

    return potencia

posInicial, posObjetivo, potencia = input().split()
posInicial = int(posInicial) - 1
posObjetivo = int(posObjetivo) - 1
potencia = int(potencia)

numNodos, numAristas = input().split()
numNodos = int(numNodos)
numAristas = int(numAristas)

pesosNodos = input().split()
for i in range(len(pesosNodos)):
    pesosNodos[i] = int(pesosNodos[i])

aristas = [[] for i in range(numNodos)]
for i in range(numAristas):
    a, b = map(int, input().split())
    aristas[int(a)-1].append(int(b-1))
    aristas[int(b)-1].append(int(a-1))


potencia = dijkstra(posInicial, posObjetivo, potencia, pesosNodos, numNodos, aristas)
print(potencia)