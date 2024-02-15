n1 = int(input("Informe um numero: "))
n2 = int(input("Informe um numero: "))
n3 = int(input("Informe um numero: "))

if n1 < n2:
    if n2 < n3:
        print("crescente")
    else:
        print("não está na ordem crescente")
else:
    print("não está na ordem crescente")