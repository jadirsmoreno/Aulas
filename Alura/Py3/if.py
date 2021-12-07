print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute = int(input("Digite o seu número: "))

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

while chute != numero_secreto:
    entrada = int(input('Digite:\n[1] Continuar\n[2] Finalizar'))
    chute = int(input("Digite o seu número: "))
    if acertou:
        print("Parabéns! Você acertou!")
    else:
        if maior:
            print("O seu chute foi maior do que o número secreto!")
        elif menor:
            print("O seu chute foi menor do que o número secreto!")

print("Fim do jogo")
