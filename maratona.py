info = input().split(' ')
pontos = input().split(' ')
saida = ''
for i in range(len(pontos)):
    pontos[i] = int(pontos[i])
for i in range(len(pontos) - 1):
    if pontos[i + 1] - pontos[i] > int(info[1]):
        saida = 'N'
        break
    else:
        saida = 'S'
print(saida)
