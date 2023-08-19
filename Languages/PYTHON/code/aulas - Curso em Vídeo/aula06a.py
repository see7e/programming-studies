n1 = input('Digite o valor:')
print(type(n1))  # TODO VALOR ADICIONADO DIRETAMENTO ATRAVÉS DO input RECEBE O type str
n2 = int(input('Digite um valor:'))
n3 = int(input('Digite vum valor:'))
print(type(n2))
s = n2 + n3
print('A soma entre', n2, "e", n3, 'é igual a', s)
# PODE-SE TAMBÉM UTILIZAR MASCARAS {} PARA INSERIR VARIÁVEIS DENTRO DO str DO COMANDO print()
print('A soma dos valores {} e {}, vale {}'.format(n2, n3, s))

print('========================  DESAFIO 04  ============================')

var = input('Digite algo:')
print(type(var))
# ABAIXO ESTÃO ALGUNS TESTES DE VERIFICAÇÃO (MÉTODOS)
print('.isalpha - ', var.isalpha())  # TESTA SE var É ALFABÉTICO
print('.isnumeric() -', var.isnumeric())  # TESTA SE var É NUMÉRICO
print('.isalnum - ', var.isalnum())  # TESTA SE var É ALFA-NUMÉRICO
print('.isupper - ', var.isupper())  # TESTA SE var ESTÁ ESCRITO EM LETRAS MAIÚSCULAS
print('.isidentifier - ', var.isidentifier())  # UMA STRING É CONSIDERADA UM IDENTIFICADOR VÁLIDO SE CONTIVER APENAS
# LETRAS ALFANUMÉRICAS (A-Z) E (0-9) OU SUBLINHADOS (_). UM
# IDENTIFICADOR VÁLIDO NÃO PODE COMEÇAR COM UM NÚMERO OU CONTER ESPAÇOS
