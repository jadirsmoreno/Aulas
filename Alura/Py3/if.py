print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
tentativas_total = 3
contador = 0
tentativas = 1

while tentativas <= tentativas_total:
    chute = int(input("Digite o seu número: "))
    print('####Tentativa {} de {}####'.format(tentativas, tentativas_total))

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    contador +=1
    tentativas += 1

    if acertou:
        print("Parabéns! Você acertou!")
        print('Você acerto em {} tentativas'.format(contador))
        break
    else:
        if maior:
            print("O seu chute foi maior do que o número secreto!")
        elif menor:
            print("O seu chute foi menor do que o número secreto!")


print("Fim do jogo")
