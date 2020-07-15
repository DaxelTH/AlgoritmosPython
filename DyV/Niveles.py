def busquedaNivel(niv, limit, inicio, fin):
    if inicio != fin:
        mid = (fin + 1 - inicio) // 2
        if int(niv[inicio + mid]) <= limit:
            inicio = inicio + mid
            return busquedaNivel(niv, limit, inicio, fin)
        elif int(niv[inicio + mid]) > limit:
            fin = fin - mid
            return busquedaNivel(niv, limit, inicio, fin)
    else:
        if int(niv[inicio]) > limit:
            inicio = inicio - 1
        return inicio


niveles = int(input())
expNivel = input().split()
numJugadores = int(input())
expNivelTotal = []
expNivelTotal.append(0)

for n in range(niveles-1):
    expNivelTotal.append(expNivelTotal[n] + int(expNivel[n]))
expNivelTotal.append(expNivelTotal[niveles-2] + int(expNivel[niveles-2]))

for n in range(numJugadores):
    expJugador = int(input())
    inicio = 0
    fin = len(expNivelTotal) - 1
    index = busquedaNivel(expNivelTotal, expJugador, inicio, fin)
    if index>niveles-1:
        print(niveles)
    else:
        print(index+1)

