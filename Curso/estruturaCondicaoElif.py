nome = input('Digite um nome: ')
idade = int(input('Digite uma idade: '))
doencaInfectoContagiosa = input('Suspeita de doença infectocontagiosa? ').upper()
if idade >= 65:
    print('O paciente {} POSSUI atendimento prioritário!'.format(nome))
elif doencaInfectoContagiosa == 'SIM':
    print('O paciente {} deve ser direcionado para a sala de espera reservada!'.format(nome))
else:
    print('O paciente {} NÃO possui atendimento prioritário e pode aguardar na sala comum!'.format(nome))
