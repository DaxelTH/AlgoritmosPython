def dijkstra(posInicial, posObjetivo, potencia, pesosNodos, numNodos, aristas):
    visitados = []
    posActual = posInicial

    vectorDist = [float("inf")] * numNodos
    visitados.append(posActual)
    vectorDist[posActual] = 0
    fin = False
    while posActual != posObjetivo and vectorDist[posActual] < potencia:
        min = float("inf")
        nodoSig = -1
        for i in range(len(aristas[posActual])):
            if not visitados.__contains__(aristas[posActual][i]):
                if posObjetivo == aristas[posActual][i]:
                    fin = True
                    break
                else:
                    if vectorDist[aristas[posActual][i]] > vectorDist[posActual] + pesosNodos[aristas[posActual][i]]:
                        vectorDist[aristas[posActual][i]] = vectorDist[posActual] + pesosNodos[aristas[posActual][i]]

        for i in range(len(vectorDist)):
            if not visitados.__contains__(i) and min > vectorDist[i]:
                min = vectorDist[i]
                nodoSig = i

        if fin:
            potencia -= vectorDist[posActual]
            return potencia

        if nodoSig != posActual:
            visitados.append(nodoSig)
            posActual = nodoSig
        else:
            potencia = 0
            return potencia

    potencia -= vectorDist[posActual]
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
if (potencia < 0): potencia = 0
print(potencia)