n = int(input("Informe o numero"))
aux = n
if n > 0:
    i = 0
    pares = 0
    impares = 0
    while i < aux:
        n = int(input("Informe o numero"))
        if n % 2 == 0:
            pares +=  1
        else:
            impares += 1
        i += 1
        
    print(pares)
    print(impares)