def busquedaAnchura(aristas, nodoQuitado, nodoSig):
    visitado = set()
    visitado.add(nodoQuitado)
    visitado.add(nodoSig)
    if len(aristas[nodoSig]) > 0:
        q = list()
        q.append(nodoSig)
        while len(q) > 0:
            # Extraemos los adyacentes de un nodo
            nodo = q.pop(0)
            for n in range(len(aristas[nodo])):
                if not visitado.__contains__(aristas[nodo][n]):
                    visitado.add(aristas[nodo][n])
                    q.append(aristas[nodo][n])

    return len(visitado)


N, M = map(int, input().strip().split())
costeNodo = []
for i in range(N):
    costeNodo.append(int(input()))

aristas = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().strip().split())
    aristas[a].append(b)
    aristas[b].append(a)


caso = [[] for i in range(N)]
criticos = set()
coste = 0
for i in range(N):
    # Quitamos cada nodo, y comprobamos que nodos se pueden visitar
    esCritico = False
    for j in range(N):
        caso[j] = aristas[j].copy()
        if j == i:
            caso[j] = []
        if caso[j].__contains__(i):
            caso[j].remove(i)
            if caso[j] == []:
                coste += costeNodo[i]
                esCritico = True

    if not esCritico:
        numVisitados = busquedaAnchura(caso, i, (i+1) % N)
        if numVisitados != N:
            coste += costeNodo[i]

print(coste)

