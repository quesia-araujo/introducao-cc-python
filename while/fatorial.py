# Escreva um programa que receba um número natural n na entrada e imprima n! (fatorial) na saída.
n = int(input("Digite o valor de n "))

fatorial = n
mult = n - 1


while(mult):
    if n == 0:
        fatorial = 1
        mult = 0
    else:
        fatorial = fatorial * mult
        mult = mult -1
    
print(fatorial)




