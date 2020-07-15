import math

def mochila(nEnemigos, psEnemigos, ataqueEnemigos, ataqueJugador):
    dañoRecibido = 0
    turnosEnemigo = []
    nTurno = 0
    for i in range(nEnemigos):
        turnosEnemigo.append(math.ceil(psEnemigos[i] / ataqueJugador))

    media = []
    for i in range(nEnemigos):
        media.append([ataqueEnemigos[i] / turnosEnemigo[i], i])

    # Ordeno array por el calculo anterior
    media.sort(reverse=True)

    for i in range(len(media)):
        enemigoAMatar = media[i][1]
        nTurno += turnosEnemigo[enemigoAMatar]
        dañoRecibido += nTurno * ataqueEnemigos[enemigoAMatar]

    print(dañoRecibido)


nCombates = int(input())
# Atacan primero enemigos
# Recibir menor daño posible
for i in range(nCombates):
    ataqueJugador = int(input())
    nEnemigos = int(input())
    ataqueEnemigos = [] * nEnemigos
    psEnemigos = [] * nEnemigos
    media = [] * nEnemigos
    ataqueEnem = input().split()
    psEnem = input().split()
    for i in range(nEnemigos):
        ataqueEnemigos.append(int(ataqueEnem[i]))
        psEnemigos.append(int(psEnem[i]))

    mochila(nEnemigos, psEnemigos, ataqueEnemigos, ataqueJugador)

