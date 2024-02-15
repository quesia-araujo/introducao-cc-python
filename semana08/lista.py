frutas_exoticas = ['jaboticaba', 'cupuaçu', 'graviola']

for fruta in frutas_exoticas:
    print('Eu adoro ' + fruta)

'''
range(inicio, fim, intervalo)
'''

for i in range(20):
    print(i)
print()
for i in range(10, 20):
    print(i)
print()
for i in range(10, 20, 2):
    print(i)

pares = range(0, 40, 2)

for item in pares:
    print(item)

animais = ['gato', 'cachorro']

for x in range(len(animais)):
    print(animais[x])

for x in range(len(animais)):
    print(x)