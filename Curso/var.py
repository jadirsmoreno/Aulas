nome = input('Digite um funcionário: ')
empresa = input('Digite uma empresa: ')
qtdadeFuncionarios = int(input('Digite a quantidade de funcionários: '))
mediaMensalidade = float(input('Digite a média da mensalidade: '))
print('{} trabalha na empresa {}'.format(nome, empresa))
print('A média de mensalidade é de: {}'.format(mediaMensalidade))
print('==================== Verifique os tipos de dados abaixo ====================')
print('o tipo da variável [nome]: {}'.format(type(nome)))
print('o tipo da variável [empresa]: {}'.format(type(empresa)))
print('o tipo da variável [quantidade de funcionários]: {}'.format(type(qtdadeFuncionarios)))
print('o tipo da variável [média mensalidade]: {}'.format(type(mediaMensalidade)))