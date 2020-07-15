def mochila (casos, nMaxDinero):
    # Calculo de beneficio / gasto
    for i in range(len(casos)):
        casos[i].append(casos[i][2] / casos[i][1])
    # Ordeno array por el calculo anterior
    casos.sort(key=elem3, reverse=True)
    sol = [0] * len(casos)
    costeAcum = 0
    benAcum = 0
    i = 0
    while costeAcum < nMaxDinero:
        if costeAcum + casos[i][1] <= nMaxDinero:
            costeAcum += casos[i][1]
            benAcum += casos[i][2]
            sol[casos[i][0]] = 1
            i += 1
        else:
            sol[casos[i][0]] = (nMaxDinero - costeAcum) / casos[i][1]
            benAcum += (casos[i][2] * sol[casos[i][0]]).__round__()
            costeAcum = nMaxDinero

    return [sol, benAcum]

def elem3(casos):
    return casos[3]


entrada1 = input().split()
nCasos = int(entrada1[0])
nMaxDinero = int(entrada1[1])
casos = []
for i in range(nCasos):
    entr = input().split()
    casos.append([i, int(entr[0]), int(entr[1])])

[sol, ben] = mochila(casos, nMaxDinero)
for i in range(nCasos):
    if sol[i] != 0:
        print(i, "", end="")

print()
print(ben)