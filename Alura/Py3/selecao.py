import forca
import numeroAleatorio

print("*********************************")
print("****** Escolha o seu jogo! ******")
print("*********************************")

print('(1) Forca\n(2) Advinhação')

jogo = int(input('Qual o jogo?'))

if jogo == 1:
    print('Jogando Forca!')
    jogar_forca()
elif jogo == 2:
    print('Jogando Advinhação!')
    jogar_advinhacao()