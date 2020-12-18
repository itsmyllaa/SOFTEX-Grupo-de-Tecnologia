###Questão criada por Stheyce do Carmo (adaptada) ] Com o passar do tempo
#os signos ganharam bastante popularidade, vindo de encontro também temos
#os Zodíaco Chinês levando em conta que não é muito visto no nosso
#cotidiano, faça um programa que ajude as pessoas a descobrirem seu signo
#do Zodíaco Chinês. O seu programa deve mostrar no final o nome da pessoa e
#o signo. Use tuplas para esse exercício e um pelo menos duas funções.
#Levando em consideração que ele é composto por animais com ciclo de 12
#anos uma maneira simples de identificar é com o ano do nascimento. Os
#signos são: (1- macaco 2-galo 3-Cão 4-Porco 5-Rato 6-Boi 7- Tigre 8-coelho 9-
#Dragão 10-Serpente 11-Cavalo 12-Carneiro).

signs = ('CARNEIRO','SERPENTE','CÃO','DRAGON','TIGRE','BOI','COELHO','RATO',
'MACACO','GALO','CAVALO','PORCO')

def zodiac():
    print('''
          ======================================
            Welcome! see your ZODIACO CHINÊS.
          ======================================
          **************************************
          1 - your ZODIACO CHINÊS
          --------------------------------------
          2 - EXIT
          --------------------------------------
          **************************************
          ''')

while True:
    zodiac()
    option = input('Faça uma escolha: ')
    print(' ')
    if option == '1':
        name = str(input('Informe seu nome: '))
        print(' ')
        year = int(input('Preencha com seu ano de nascimento: '))
        print(' ')
        signs = signs[year%12]
        print(f'{name}, O SEU SIGNO DO ZODIACO CHINÊS É: {signs}.')
        print(' ')
        break

    elif option =='2':
        break