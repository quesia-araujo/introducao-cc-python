fora = 5
soma = 0
while fora > 0:
    dentro = 0
    while dentro < fora:
        print('oi')
        soma += 1
        dentro = dentro + 1
    print()
    fora -= 1
print(soma)