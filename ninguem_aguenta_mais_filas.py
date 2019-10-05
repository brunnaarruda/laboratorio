n = int(input())
listaN = [int (x) for x in input().split()]
m = int(input())
listaM = [int (x) for x in input().split()]

for x in range(m):
    listaN.remove(listaM[x])
for x in listaN:
    if x==listaN[-1]:
        print(x)
    else:
        print(x,end=' ')