'''
Dado um número inteiro m, n> 1, imprimir sua decomposição em fatores primos,  indicando também a multiplicidade  de cada fator
'''

n = int(input('Digite um numero inteiro maior que 1'))

fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
        multiplicidade += 1
        n /= fator
    if multiplicidade > 0:
        print('O fator', fator, 'multiplicidade = ', multiplicidade)
    fator += 1
    multiplicidade = 0