#   AULA 07
#   OPERADORES ARITIMÉTRICOS
a = int(input('Digite um valor:'))
b = int(input('Digite um valor:'))

soma = a + b        # SOMA ENTRE NUM OU VAR
sub = a - b         # SUBTRAÇÃO ENTRE NUM OU VAR
mult = a * b        # MULTIPLICAÇÃO ENTRE NUM OU VAR
div = a / b         # DIVISÃO ENTRE NUM OU VAR
pot = a ** b        # POTENCIAÇÃO ENTRE NUM OU VAR
di = a // b         # RETORNA VALOR INTEIRO DA DIVISÃO ENTRE NUM OU VAR
mod = a % b         # RETORNA VALOR INT DO RESTO DA DIVISÃO, SEM CALCULAR CASAS DECIMAIS

print('A soma é {}, a subtração é {},\nA multiplicação {:.3f}, a divião {:.3f}'.format(soma, sub, mult, div), end=' ')
#   O \n QUEBRA A LINHA
#   O end='' JUNTA DUAS LINHAS SEPARADAS
print('a divisão int é {} e o resto da divisão é {}'.format(di, mod))

#   ORDEM DE PRECEDÊNCIA
#   1o - ()
#   2o - **
#   3o - *  /  //  %
#   4o - +  -

#   DESAFIO 05
print('=== DESAFIO05 ===')
c = int(input('Digite um número:'))
print('O seu sucessor é {}, e seu antecessor é {}'.format(c+1, c-1))

#   DESAFIO 06
print('=== DESAFIO 06 ===')
d = int(input('Digite um valor:'))
print('tem dobro igual a {}, triplo igual a {}, e raiz igual a {}'.format(d*2, d*3, d**(1/2)))

#   DESAFIO 07
print('=== DESAFIO 07 ===')
n1 = int(input('Primeira nota:'))
n2 = int(input('Segunda nota:'))
med = (n1+n2)/2
print(med)

#   DESAFIO 08
print('=== DESAFIO 08 ===')
met = float(input('Qual a metragem?'))
print('O resultado em cm é {} e em mm é {}'.format(met*100, met*1000))

#   DESAFIO 09
print('=== DESAFIO 09 ===')
x = int(input('Digite para tabuada:'))
x2 = x*2
x3 = x*3
x4 = x*4
x5 = x*5
x6 = x*6
x7 = x*7
x8 = x*8
x9 = x*9
x10 = x*10
print('A tabuada de {} é\n{} {} {} {} {}\n{} {} {} {} {}'.format(x, x, x2, x3, x4, x5, x6, x7, x8, x9, x10))

#   DESAFIO 10
print('=== DESAFIO 10 ===')
din = float(input('Quanto você tem? '))
print('Voce tem o equivalente a {} dolares'.format(din/3.27))

#   DESAFIO 11
print('=== DESAFIO 11 ===')
larg = float(input('Largura:'))
alt = float(input('Altura:'))
area = larg*alt
print('Será necessário o uso de {} latas de tinta'.format(area))

#   DESAFIO 12
print('=== DESAFIO 12 ===')
val = float(input('Preço de produto:'))
preco = val*.95
print('Você pode pagar {}, com 5% de desconto'.format(preco))

#   DESAFIO 13
print('=== DESAFIO 13 ===')
sal = float(input('Qaul seu salário:'))
print('Seu salario agora é de {} reais, com um aumento de 15%'.format(sal*1.15))
