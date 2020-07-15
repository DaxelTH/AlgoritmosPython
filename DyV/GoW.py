def busquedaNivel3(niv, player, inicio, fin):
    if inicio != fin:
        mid = (fin + 1 - inicio)//2
        if int(niv[inicio + mid]) <= player:
            inicio = inicio + mid
            return busquedaNivel3(niv, player, inicio, fin)
        elif int(niv[inicio + mid]) > player:
            fin = fin - mid
            return busquedaNivel3(niv, player, inicio, fin)
    else:
        if int(niv[inicio]) > player:
            inicio = inicio - 1
        return inicio

numNiveles = int(input())
niveles = input().split()
numJugadores = int(input())
jugadores = input().split()

if (numNiveles > 0):
    for n in range(numJugadores):
        jugador = int(jugadores[n])
        if jugador < int(niveles[0]):
            print ("X " + niveles[0])
        elif jugador > int(niveles[len(niveles)-1]):
            print(niveles[len(niveles)-1] + " X")
        elif jugador == int(niveles[0]):
            print("X " + niveles[1])
        elif jugador > int(niveles[len(niveles)-1]):
            print(niveles[len(niveles) - 2] + " X")
        else:
            pos = busquedaNivel3(niveles, jugador, 0, len(niveles)-1)

            if pos == -1:
                if int(niveles[0]) == jugador:
                    print("X " + niveles[1])
                else:
                    print("X " + niveles[0])
            elif pos == len(niveles)-1:
                if int(niveles[len(niveles)-1]) == jugador:
                    print(niveles[len(niveles)-1-1] + " X")
                else:
                    print(niveles[len(niveles)-1] + " X")
            else:
                if int(niveles[pos]) == jugador:
                    if pos - 1 >= 0 and pos + 1 <= len(niveles):
                        print(niveles[pos-1] + " " + niveles[pos+1])
                    elif pos - 1 >=0:
                        print(niveles[pos-1] + " X")
                    else:
                        print("X " + niveles[pos + 1])
                else:
                    print(niveles[pos] + " " + niveles[pos+1])

