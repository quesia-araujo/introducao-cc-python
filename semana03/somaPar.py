n = int(input("Informe o numero"))
aux = n
if n > 0:
    i = 0
    soma = 0
    while i < aux:
        n = int(input("Informe o numero"))
        if n % 2 == 0:
            soma = soma + n
        i = i + 1
    print(soma)
