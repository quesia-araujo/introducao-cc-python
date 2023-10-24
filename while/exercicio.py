n = int(input('Digite um número: '))

while n >= 0:
    fatorial = 1 # elemento neutro da multiplicação
    while (n > 1):
        fatorial *= n
        n = n -1
    print(fatorial)
    n = int(input('Digite um número: '))
