n_registros = int(input())
amigos = []
eventos = []
for c in range(0, n_registros):
    temp_etapa, temp_valor = input().split()
    temp_etapa = str(temp_etapa).upper()
    temp_valor = int(temp_valor)
    eventos.append(temp_etapa)

    if temp_etapa == 'R':
        presente = False
        for elemento in amigos:
            if elemento[2] > 0 and eventos[-2] != 'T':
                elemento[1] += 1
            if elemento[0] == temp_valor:
                elemento[2] += 1
                presente = True
        if not presente:
            amigos.append([temp_valor, 0, 1])
            amigos.sort()

    elif temp_etapa == 'E':
        for elemento in amigos:
            if elemento[0] == temp_valor:
                if eventos[-2] != 'T':
                    elemento[1] += 1
                elemento[2] -= 1
            elif elemento[2] > 0 and eventos[-2] != 'T':
                elemento[1] += 1

    elif temp_etapa == 'T':
        for elemento in amigos:
            if elemento[2] > 0:
                elemento[1] += temp_valor

for elemento in amigos:
    if elemento[2] > 0:
        elemento[1] = -1
    print(f'{elemento[0]} {elemento[1]}')
