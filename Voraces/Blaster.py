def dijkstra(posInicial, posObjetivo, potencia, pesosNodos, aristas):
    visitados = []

    vectorDist = [float("inf")] * (len(pesosNodos) - 1)

    init = posInicial
    fin = posObjetivo

    nodoSig = -1
    posActual = posInicial
    # Pasos
    while potencia > 0 or posActual != fin:
        # Actualizo el vector de distancias desde la posición en la que estoy
        min = float("inf")
        for i in range(len(aristas[posActual-1])):
            vectorDist[aristas[posActual-1][i]-1] = pesosNodos[aristas[posActual-1][i]-1]
            if min > vectorDist[aristas[posActual-1][i]-1] or nodoSig == -1:
                min = vectorDist[aristas[posActual-1][i]-1]
                nodoSig = aristas[posActual - 1][i] - 1

        posActual = nodoSig
        potencia -= min

    return potencia

posInicial, posObjetivo, potencia = input().split()
posInicial = int(posInicial)
posObjetivo = int(posObjetivo)
potencia = int(potencia)

numNodos, numAristas = input().split()
numNodos = int(numNodos)
numAristas = int(numAristas)

pesosNodos = input().split()
for i in range(len(pesosNodos)):
    pesosNodos[i] = int(pesosNodos[i])

aristas = [[] for i in range(numNodos)]
for i in range(0, numAristas):
    a, b = map(int, input().split())
    aristas[int(a)-1].append(int(b))
    aristas[int(b)-1].append(int(a))

print(aristas)
potencia = dijkstra(posInicial, posObjetivo, potencia, pesosNodos, aristas)
print (potencia)