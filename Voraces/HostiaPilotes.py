def busquedaAnchura(aristas):
    coste = 0
    visitado = set()
    for i in range(len(aristas)):
        if not visitado.__contains__(i):
            coste += 1
            visitado.add(i)
            if len(aristas[i]) > 0:
                q = []
                q.append(i)
                while len(q) > 0:
                    # Extraemos los adyacentes de un nodo
                    nodo = q.pop(0)
                    for n in range(len(aristas[nodo])):
                        if not visitado.__contains__(aristas[nodo][n]):
                            visitado.add(aristas[nodo][n])
                            q.append(aristas[nodo][n])

    return coste

nPilotes, nPares = input().split()
nPilotes = int(nPilotes)
nPares = int(nPares)

aristas = [[] for i in range(nPilotes)]
for i in range(nPares):
    a, b = input().split()
    aristas[int(a)].append(int(b))
    aristas[int(b)].append(int(a))

coste = busquedaAnchura(aristas)
print(coste)
