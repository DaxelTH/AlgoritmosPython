def rellenarMochila(casos, W):
    casos = densidadValorCaso(casos)
    casos = ordenar(casos)
    solucion = [0] * len(casos)
    peso = 0
    i = 0
    while peso < W:
        if peso + casos[i][1] <= W:
            peso += casos[i][1]
            solucion[casos[i][0]] = 1
            i+=1
        else:
            solucion[casos[i][0]] = (W-peso) / casos[i][1]
            peso = W
    return solucion


def densidadValorCaso(casos):
    for i in range(len(casos)):
        casos[i].append(casos[i][2] / casos[i][1])
    return casos


def ordenar(casos):
    for j in range(1, len(casos)):
        clave = casos[j][:]
        i = j-1
        while i >= 0 and casos[i][3] < clave[3]:
            casos[i+1][:] = casos[i][:]
            i = i-1
            casos[i+1][:] = clave[:]
    return casos


entrada1 = input().split()
nCasos = int(entrada1[0])
nMaxDinero = int(entrada1[1])
casos = []
preCasos = []
for i in range(nCasos):
    entr = input().split()
    casos.append([i, int(entr[0]), int(entr[1])])
    preCasos.append([i, int(entr[0]), int(entr[1])])

resultado = rellenarMochila(casos, nMaxDinero)
dinero = 0
for i in range(nCasos):
    if resultado[i] != 0:
        print(i, "", end="")
        dinero += preCasos[i][2] * resultado[i]

print()
print(dinero.__round__())