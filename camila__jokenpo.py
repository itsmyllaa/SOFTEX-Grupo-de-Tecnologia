from random import randint
from time import sleep
Score1 = 0
Score2 = 0
c = 0
lista = ("Pedra", "Papel", "Tesoura")
print(' ')
Nickname1 = str(input('1º jogador, digite seu nickname: '))
print(' ')
Nickname2 = str(input('2º jogador, digite seu nickname: '))
print(' ')
while (Score1 > 0 or Score2 < 2) and (Score1 < 2 or Score2 > 0) and (c < 3):
    print(' ')
    Player1 = int(input('''1º jogador, escolha uma das opções abaixo: 
    [0] Pedra
    [1] Papel
    [2] Tesoura
    Digite sua escolha: '''))
    print(' ')
    Player2 = int(input('''2º jogador, escolha uma das opções abaixo: 
    [0] Pedra
    [1] Papel
    [2] Tesoura
    Digite sua escolha: '''))
    print("---JO...---\n")
    sleep(1)
    print("---KEN...---\n")
    sleep(1)
    print("---POOH!!!---\n")
    print("-="*20)
    print(Nickname2, " escolheu: {}".format(lista[Player2]))
    print(Nickname1, " escolheu: {}".format(lista[Player1]))
    print("-="*20)

    if Player2 == 0:
        if Player1 == 0:
            print("Empate!, HAHA.")
        elif Player1 == 1:
            print(Nickname1, " venceu, ", Nickname2, " ... que pena não foi dessa vez!")
            Score1 += 1
            c += 1
        elif Player1 == 2:
            print(Nickname2, " venceu, ", Nickname1, " ... que pena não foi dessa vez!")
            Score2 += 1
            c += 1
        else:
            print("Operação inválida!")

    elif Player2 == 1:
        if Player1 == 0:
            print(Nickname2, " venceu, ", Nickname1," ... que pena não foi dessa vez!")
            Score2 += 1
            c += 1
        elif Player1 == 1:
            print("Empate!")
        elif Player1 == 2:
            print(Nickname1, " venceu, ", Nickname2, " ... que pena não foi dessa vez!")
            Score1 += 1
            c += 1
        else:
            print("Operação inválida!")
    elif Player2 == 2:
        if Player1 == 0:
            print(Nickname1, " Venceu, ", Nickname2, "... que pena não foi dessa vez!")
            Score1 += 1
            c += 1
        elif Player1 == 1:
            print(Nickname2, " venceu, ", Nickname1, "... que pena não foi dessa vez!")
            Score2 += 1
            c += 1
        elif Player1 == 2:
            print("Empate!")
        else:
            print("Operação inválida!")
    else:
            print("Operação inválida!")
print(' ')
if (Score1 == 2) and (Score1 > Score2):
    print('PARABÉNS!!! --- ', Nickname1, 'VOCÊ É O VENCEDOR DO JOGO COM ', Score1, 'PONTOS!')
elif (Score2 == 2) and (Score2 > Score1):
    print('PARABÉNS!!! --- ', Nickname2, 'VOCÊ É O VENCEDOR DO JOGO COM ', Score2, 'PONTOS!')