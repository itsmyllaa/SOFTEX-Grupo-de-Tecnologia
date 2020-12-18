signos = ('CARNEIRO','SERPENTE','CÃO','DRAGON','TIGRE','BOI','COELHO','RATO',
'MACACO','GALO','CAVALO','PORCO')

def zodiac():
    print('''
          **
            Welcome! VEJA SEU ZODIACO CHINES.
          **
          1 - SEU ZODIACO CHINÊS
          ========================
          2 - SAIR
          **
          ''')

while True:
    zodiac()
    opc = input('Faça uma escolha: ')
    print(' ')
    if opc == '1':
        nome = str(input('Informe seu nome: '))
        print(' ')
        ano = int(input('Preencha com seu ano de nascimento: '))
        print(' ')
        signos = signos[ano%12]
        print(f'{nome}, O SEU SIGNO DO ZODIACO CHINÊS É: {signos}.')
        print(' ')
        break

    elif opc =='2':
        break