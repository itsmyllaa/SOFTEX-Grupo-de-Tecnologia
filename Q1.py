####Lurdes tem um brechó e quer um programa que armazene todas as suas peças com seus respectivos preços, 
# quantidade da peça e que ela possa excluir e incluir itens depois. Use uma lista ou lista composta para 
# armazenar o nome do item, o preço e a quantidade. Faça um menu com opções de incluir e excluir os itens 
# (que forem vendidos). No final o programa deve mostrar os itens vendidos (excluídos), 
# a lista com os itens cadastrados( apenas aqueles que não foram vendidos e o total vendido.


pecas = list()
vendidos = list()
total = 0
op = 1

while op != 0:
    print("MENU DE ITENS")
    print("0- SAIR")
    print("1- INCLUIR")
    print("2- EXCLUIR")

    op = int(input())

    if op == 1:
        a = int(input("QUANTOS VOCÊ QUER INCLUIR? "))
        for i in range(0,a):
            cadastro = [input("INSIRA O NOME: "),float(input("Inserir Preço: ")),int(input("Inserir Quantidade: "))]
            pecas.append(cadastro)

    elif op == 2:
        print(pecas)
        nome = input("Insira Nome: ")
        for j in range(0,len(pecas)):
            if nome in pecas[j][0]:
                vendidos.append(pecas[j])
                total = 1+1
                pecas[j][2]-=1


print("VENDIDOS")
for h in range(0,len(vendidos)):
    print(vendidos[h])
print("ITENS EM ESTOQUE")
for h in range(0,len(pecas)):
    print(pecas[h])

print("TOTAL DE VENDAS: ",total)