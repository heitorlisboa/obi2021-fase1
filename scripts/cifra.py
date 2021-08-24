P = input().lower()
letras_p_cifrada = [letra for letra in P]
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z']
vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z']

def calculador_distancia_vogal(letra):
    pos_conso = alfabeto.index(letra)
    for vogal in vogais:
        pos_vog = alfabeto.index(vogal)
        if pos_vog > pos_conso:
            distancia = pos_vog - pos_conso
        else:
            distancia = pos_conso - pos_vog
        if vogal == 'a':
            menor_dist = distancia
            prox = vogal
        elif distancia < menor_dist:
            menor_dist = distancia
            prox = vogal
    return prox


def calculador_distancia_conso(letra):
    if letra != 'z':
        prox_conso = consoantes.index(letra) + 1
    else:
        prox_conso = consoantes.index(letra)
    return consoantes[prox_conso]


for index in range(0, len(letras_p_cifrada)):
    temp_letra = letras_p_cifrada[index]
    if temp_letra in consoantes:
        letras_p_cifrada[index] += calculador_distancia_vogal(temp_letra)
        letras_p_cifrada[index] += calculador_distancia_conso(temp_letra)

palavra_cifrada = ''.join(letras_p_cifrada)
print(palavra_cifrada)
