N = int(input())
lista = []
soma = 0

def Fatorial(numero):
    fatorial = 1
    for i in range(numero):
        fatorial = fatorial * int(numero-i)
    return fatorial

def Achar(N,lista,soma):
    num = 9
    for i in range(9):
        numero= num-i
        fatorial = Fatorial(numero)
        fatorialAnterior = Fatorial(numero-1)
        if (fatorial+soma) > N and (fatorialAnterior+soma) < N:
            lista.append(fatorialAnterior)
            soma+= fatorialAnterior
            return Achar(N,lista,soma)
        elif fatorial+soma == N:
            lista.append(fatorial)
            soma+=fatorial
            return len(lista)


saida = Achar(N,lista,soma)
print(saida)