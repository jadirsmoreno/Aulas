import forca
import numeroAleatorio

print("*********************************")
print("****** Escolha o seu jogo! ******")
print("*********************************")

print('(1) Forca\n(2) Advinhação')

jogo = int(input('Qual o jogo?'))

if jogo == 1:
    print('Jogando Forca!')
elif jogo == 2:
    print('Jogando Advinhação!')
