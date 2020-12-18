###Questão criada por Nicolas Mathias (adaptada)] Cinco amigos saíram para
#jantar fora e nessa noite ficou definido que seria feito um sorteio para quem
#iria pagar a conta. Para isso faça um dicionário com os nomes dos amigos,
#faça um sorteio dentre esses para ver quem vai pagar a conta. Além disso, seu
#programa deve pegar o valor da conta que pode ser adiciono os 10% do
#garçom.

import random
import math

quantities = 5

names = {}

print('-----------')
check = float(input('QUAL O VALOR DA CONTA: R$'))
print('----------')
for i in range(quantities):
    names[i] = str(input('QUEM VAI PARTICIPAR: '))
    print('----------')

def valueTip(valueCheck, payTip ,taxa = 0.10):
    if payTip == 'S':
        return check*0.10
    return 0

valid = ('S','N')
pay = None


while not pay in valid:
    print('------------')
    pay = input('DESEJA PAGAR A GORJETA? [S/N] ').upper()
    print('------------')

print('------------')
print('O NÚMERO DE CADA UM É: ')
print(names)
print('-------------')

draw = math.ceil((quantities - 1) * (random.random()))

print(f'O NÚMERO SORTEADO FOI: {draw}')
print(names[draw],' IRÁ PAGAR A CONTA.')
print('------------')
print(f'\nVALOR DA GORJETA: R$ {valueTip(check,pay)}')
print(f'TOTAL DA CONTA {valueTip(check,pay)+check}')
print('------------')
