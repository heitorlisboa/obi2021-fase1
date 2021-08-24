idade1 = int(input())
idade2 = int(input())
idade3 = int(input())
idades = [idade1, idade2, idade3]
condição = True
for num in idades:
    if not 5 <= num <= 100:
        condição = False

if condição:
    idades.sort()
    print(idades[1])
