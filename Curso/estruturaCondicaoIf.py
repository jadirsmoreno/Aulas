nome = input('Digite um nome: ')
idade = int(input('Digite uma idade: '))
if idade >= 65:
    print('O paciente {} possui atendimento prioritário!'.format(nome))
else:
    print('O paciente {} não possui atendimento prioritário!'.format(nome))
