import math

def backtracking(jugadores, solucion, mejorSol, equipos):
    if len(jugadores) == 0:
        if equipos[0] != 0 and equipos[1] != 0 and equipos[2] != 0:
            solucion = max(math.fabs(equipos[0] - equipos[1]), math.fabs(equipos[0] - equipos[2]), math.fabs(equipos[1] - equipos[2]))
            mejorSol = min(solucion, mejorSol)
            return mejorSol
    else:
        i = 0
        while i < 3 and len(jugadores) != 0:
            equipos[i] += jugadores[0]
            jug = jugadores.pop(0)
            mejorSol = backtracking(jugadores, solucion, mejorSol, equipos)
            jugadores.append(jug)
            equipos[i] -= jug
            i += 1
    return mejorSol


nJugadores = int(input())
jug = input()
jugadores = list(map(int, jug.split()))

equipos = [0 for i in range(3)]
mejorSol = float("inf")
solucion = float("inf")
mejorSol = backtracking(jugadores, solucion, mejorSol, equipos)
print(int(mejorSol))
