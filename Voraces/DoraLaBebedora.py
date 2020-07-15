ent = input().split()
nPociones = int(ent[0])
tMax = int(ent[1])
pociones = []
for i in range(nPociones):
    pociones.append(int(input()))

pociones.sort()
i = 0
sumaMax = 0
while i < len(pociones):
    sumaMax += pociones[i] * (nPociones - i)
    if sumaMax > tMax:
        print("Dora")
        break
    i += 1

if sumaMax <= tMax:
    print("AleG")
