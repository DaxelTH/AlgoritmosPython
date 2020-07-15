import math

def backtracking(jugadores, solucion, mejorSol, media, equipos):
    if len(jugadores) == 0:
        if equipos[0] != 0 and equipos[1] != 0 and equipos[2] != 0:
            solucion = max(math.fabs(equipos[0] - equipos[1]), math.fabs(equipos[0] - equipos[2]), math.fabs(equipos[1] - equipos[2]))
            mejorSol = min(solucion, mejorSol)
            return mejorSol
    else:
        i = 0
        while i < 3 and len(jugadores) > 0:
            if esFactible(jugadores[0], equipos[i], media):
                equipos[i] += jugadores[0]
                jug = jugadores.pop(0)
                backtracking(jugadores, solucion, mejorSol, media, equipos)
                jugadores.append(jug)
                equipos[i] -= jug
            i += 1
    return mejorSol


def esFactible(jugador, equipo, media):
    #if jugador + equipo <= media:
        return True
    #return False


nJugadores = int(input())
jug = input()
jugadores = list(map(int, jug.split()))

nivelTotal = 0
for i in range(nJugadores):
    nivelTotal += jugadores[i]

media = nivelTotal//3
equipos = [0 for i in range(3)]
mejorSol = float("inf")
solucion = float("inf")
mejorSol = backtracking(jugadores, solucion, mejorSol, media, equipos)
print(mejorSol)

