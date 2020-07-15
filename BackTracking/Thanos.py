def backtracking(nPlanetas, planetaActual, visitados, aristas, solucion, soluciones):
    if len(visitados) == nPlanetas:
        soluciones.append(1)
    else:
        for i in range(len(aristas[planetaActual])):
            if len(visitados) != nPlanetas - 1:
                if aristas[planetaActual][i] not in visitados and aristas[planetaActual][i] != 0:
                    solucion.append(aristas[planetaActual][i])
                    visitados.add(aristas[planetaActual][i])
                    backtracking(nPlanetas, aristas[planetaActual][i], visitados, aristas, solucion, soluciones)
                    visitados.remove(aristas[planetaActual][i])
                    solucion.remove(aristas[planetaActual][i])
            else:
                if aristas[planetaActual][i] == 0:
                    visitados.add(aristas[planetaActual][i])
                    solucion.append(aristas[planetaActual][i])
                    backtracking(nPlanetas, aristas[planetaActual][i], visitados, aristas, solucion, soluciones)
                    visitados.remove(aristas[planetaActual][i])
                    solucion.remove(aristas[planetaActual][i])
    return soluciones


nPlanetas, nConexiones = list(map(int, input().split()))
aristas = [[] for i in range(nPlanetas)]

for i in range(nConexiones):
    a, b = list(map(int, input().split()))
    aristas[a].append(b)
    aristas[b].append(a)

visitados = set()
solucion = []
soluciones = []

soluciones = backtracking(nPlanetas, 0, visitados, aristas, solucion, soluciones)
print(len(soluciones))
