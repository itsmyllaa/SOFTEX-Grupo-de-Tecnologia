###Questão criada por Nicolas Mathias (adaptada)] Cinco amigos saíram para
#jantar fora e nessa noite ficou definido que seria feito um sorteio para quem
#iria pagar a conta. Para isso faça um dicionário com os nomes dos amigos,
#faça um sorteio dentre esses para ver quem vai pagar a conta. Além disso, seu
#programa deve pegar o valor da conta que pode ser adiciono os 10% do
#garçom.

import random
import math

nomes = {}

quantidade = 5

print(' ')
conta = float(input('QUAL O VALOR DA CONTA: R$'))
print(' ')
for i in range(quantidade):
    nomes[i] = str(input('QUEM VAI PARTICIPAR: '))
    print(' ')

def valorGorjeta(valorconta, pagarGorj ,taxa = 0.10):
    if pagarGorj == 'S':
        return conta*0.10
    return 0

valid = ('S','N')
pagar = None


while not pagar in valid:
    print(' ')
    pagar = input('DESEJA PAGAR A GORJETA? [S/N] ').upper()
    print(' ')

print(' ')
print('O NÚMERO DE CADA UM É: ')
print(nomes)
print(' ')

sorteio = math.ceil((quantidade - 1) * (random.random()))

print(f'O NÚMERO SORTEADO FOI: {sorteio}')
print(nomes[sorteio],' IRÁ PAGAR A CONTA.')
print(' ')
print(f'\nVALOR DA GORJETA: R$ {valorGorjeta(conta,pagar)}')
print(f'TOTAL DA CONTA {valorGorjeta(conta,pagar)+conta}')
print(' ')
