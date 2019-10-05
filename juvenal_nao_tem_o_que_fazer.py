def F(n, cont=0):
    if n == 1:
        cont += 1
        return cont
    elif n % 2 == 0:
        cont += 1
        return F(n / 2, cont)
    elif n % 2 != 0:
        cont += 1
        return F((3 * n) + 1, cont)


lista = []
entrada = int(input())
for i in range(entrada):
    add = input().split()
    for i in range(len(add)):
        add[i] = int(add[i])
    lista.append(add)
maximos = []
for i in range(len(lista)):
    maxx = []
    for j in range(lista[i][0], lista[i][1] + 1):
        a = F(j)
        maxx.append(a)
    m = max(maxx)
    maximos.append(m)
    maxx = []

for i in range(len(maximos)):
    print('Caso %i: %i' % (i + 1, maximos[i]))