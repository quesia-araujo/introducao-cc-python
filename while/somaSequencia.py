print("Digite uma sequencia de valores terminada em zero.")

soma = 0
valor = 1
while valor != 0:
    valor = int(input("Digite um valor a ser somado:"))
    soma = soma + valor
print(soma)