tabuada = int(input('Digite um número para exibir a tabuada: '))
print('Tabuada do número {}'.format(tabuada))
for valor in range (1, 11, 1):
    print('{} x {:2} = {}'.format(tabuada, valor, tabuada*valor, end=' '))