from random import randrange

def numero_aleatorio():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = randrange(1, 101)  # importa um número aleatório entre 1 e 100
    total_de_tentativas = 0
    pontos = 1000

    print(numero_secreto)

    print("Qual nível de dificuldade?\n(1) Fácil\n(2) Médio\n(3) Difícil")
    nivel = int(input("Escolha seu nível: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

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
            print(f'Parabéns! Você acertou!\nSua pontuação foi de {pontos}')
            break

        else:
            if maior:
                print('O seu chute foi maior do que o número secreto!')
            elif menor:
                print('O seu chute foi menor do que o número secreto!')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("o número secreto era: {}".format(numero_secreto))
    print("Fim do jogo")
