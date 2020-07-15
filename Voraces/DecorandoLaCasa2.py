def dijkstra(posInicial, numNodos, aristas):
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


nHabitaciones, nPuertas, tMax = input().split()
nHabitaciones = int(nHabitaciones)
nPuertas = int(nPuertas)
tMax = int(tMax)

aristas = [[] for i in range(nHabitaciones)]
for i in range(nPuertas):
    a, b, z = input().split()
    aristas[int(a)].append([int(b), int(z)])
    aristas[int(b)].append([int(a), int(z)])

vectorDist = dijkstra(0, nHabitaciones, aristas)
coste = 0
for i in range(len(vectorDist)):
    coste += vectorDist[i]
    if coste > tMax:
        break

if coste > tMax:
    print("Aleg, ¡a decorar!")
else:
    print(coste)