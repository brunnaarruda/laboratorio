num = int(input())
pecas = input().split(' ')
for i in range(len(pecas)):
     pecas[i] = int(pecas[i])
for j in range(len(pecas)):
     if (j+1) not in pecas:
          print(j+1)