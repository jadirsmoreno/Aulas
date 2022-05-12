import forca
import numeroAleatorio


def escolha_jogos():
    print("*********************************")
    print("****** Escolha o seu jogo! ******")
    print("*********************************")

    print('(1) Forca\n(2) Adivinhação')

    jogo = int(input('Qual o jogo?'))

    if jogo == 1:
        print('Jogando Forca!')
        forca.jogar_forca()
    elif jogo == 2:
        print('Jogando Adivinhação!')
        numeroAleatorio.jogar_numero_aleatorio()


if (__name__ == "__main__"):
    escolha_jogos()
