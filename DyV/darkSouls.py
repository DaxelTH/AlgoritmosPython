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

enemOleada = int(input())
dañoOleada = input().split()
casos = int(input())
nivelOleadaTotal = []
nivelOleadaTotal.append(0)
for n in range(enemOleada):
    nivelOleadaTotal.append(nivelOleadaTotal[n] + int(dañoOleada[n]))
nivelOleadaTotal.append(nivelOleadaTotal[enemOleada] + int(dañoOleada[enemOleada-1]))

for n in range(casos):
    astora = int(input())
    if (int(dañoOleada[0]) > astora):
        numMuertos = 0
        suma = 0
    elif (int(dañoOleada[len(dañoOleada)-1]) < astora):
        numMuertos = enemOleada
        suma = nivelOleadaTotal[numMuertos]
    else:
        inicio = 0
        fin = len(dañoOleada)-1
        nivelMuertos = busquedaNivel(dañoOleada, astora, inicio, fin)
        numMuertos = nivelMuertos+1
        suma = nivelOleadaTotal[numMuertos]

    print(numMuertos, suma)
