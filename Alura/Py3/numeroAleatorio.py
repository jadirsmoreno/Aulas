from random import randrange

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = randrange(1, 100)
total_de_tentativas = 3

print(numero_secreto)

for rodada in range(1, total_de_tentativas + 1):
    print('####Tentativa {} de {}####'.format(rodada, total_de_tentativas))
    chute = int(input('Digite o seu número, entre 1 e 100: '))

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if chute < 1 or chute > 100:
        print("Você deve digitar entre 1 e 100!")
        continue

    if acertou:
        print('Parabéns! Você acertou!')
        break

    else:
        if maior:
            print('O seu chute foi maior do que o número secreto!')
        elif menor:
            print('O seu chute foi menor do que o número secreto!')
print("o número secreto era: {}".format(numero_secreto))
print("Fim do jogo")
