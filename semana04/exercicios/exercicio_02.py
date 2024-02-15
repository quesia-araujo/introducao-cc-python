'''
Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente. O programa deve imprimir, usando repetições encaixadas (laços aninhados), uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.

Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.
'''
largura = int(input("Digite a largura do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))

i = 0
while i < altura:
    j = 0
    while j < largura:
        if i == 0 or i == altura - 1 or j == 0 or j == largura - 1:
            print('#', end='')
        else:
            print(' ', end='')
        j += 1
    print()  
    i += 1


