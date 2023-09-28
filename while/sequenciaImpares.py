n = int(input("Digite o valor de n"))
# Receba um número inteiro positivo na entrada e imprima os  n primeiros números ímpares naturais. 
contador = 0
numeros = 1

while(contador  <  n):
    if numeros % 2 != 0:
        print(numeros)
        contador+=1
    
    numeros+=1
    
    

