####Lurdes tem um brechó e quer um programa que armazene todas as suas peças com seus respectivos preços, 
# quantidade da peça e que ela possa excluir e incluir itens depois. Use uma lista ou lista composta para 
# armazenar o nome do item, o preço e a quantidade. Faça um menu com opções de incluir e excluir os itens 
# (que forem vendidos). No final o programa deve mostrar os itens vendidos (excluídos), 
# a lista com os itens cadastrados( apenas aqueles que não foram vendidos e o total vendido.


parts = list()
sold = list()
total = 0
options = 1

while options != 0:
    print("=============")
    print("MENU DE ITENS")
    print("=============")
    print("*************")
    print("0- SAIR")
    print("1- INCLUIR")
    print("2- EXCLUIR")
    print("*************")

    options = int(input())

    if options == 1:
        a = int(input("QUANTOS VOCÊ QUER INCLUIR? "))
        for i in range(0,a):
            register = [input("NOME DA PEÇA: "),float(input("PREÇO DA PEÇA: ")),int(input("QUANTIDADE DA PEÇA: "))]
            parts.append(register)

    elif options == 2:
        print(parts)
        name = input("NOME DA PEÇA QUE DESEJA REMOVER: ")
        print("*********************************")
        for j in range(0,len(parts)):
            if name in parts[j][0]:
                sold.append(parts[j])
                total = 1+1
                parts[j][2]-=1


print("VENDIDOS:")
print("******************")
for h in range(0,len(sold)):
    print(sold[h])
print("ITENS EM ESTOQUE:")
print("******************")
for h in range(0,len(parts)):
    print(parts[h])

print("TOTAL DE VENDAS: ",total)
print("******************")