quantidade_num = int(input())
if 1 <= quantidade_num <= 100000:
    lista_num = []
    for c in range(0, quantidade_num):
        temp_num = int(input())
        if 0 < temp_num <= 100:
            lista_num.append(temp_num)
        elif temp_num == 0:
            lista_num.pop()
    if 0 <= sum(lista_num) <= 1000000:
        print(sum(lista_num))
