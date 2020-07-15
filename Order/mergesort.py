def mergeSort(lista):
    if len(lista)>1:
        mid = len(lista)//2
        mitadIzq = lista[:mid]
        mitadDer = lista[mid:]

        mergeSort(mitadIzq)
        mergeSort(mitadDer)

        i=0
        j=0
        k=0
        while i < len(mitadIzq) and j < len(mitadDer):
            if int(mitadIzq[i]) <= int(mitadDer[j]):
                lista[k] = mitadIzq[i]
                i=i+1
            else:
                lista[k] = mitadDer[j]
                j=j+1
            k=k+1

        while i < len(mitadIzq):
            lista[k] = mitadIzq[i]
            i=i+1
            k=k+1

        while j < len(mitadDer):
            lista[k] = mitadDer[j]
            j=j+1
            k=k+1

num = int(input())
array = []
array = input().split()
mergeSort(array)
for n in range(num-1):
    print(array[n] + " ",end="")
print(array[num-1])