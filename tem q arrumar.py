mochila= []
while True:
    opcao = int(input("escolha uma opção: \n 1 - add item \n 2 - remover item \n 3 - modificar item \n 4 - fechar a mochila \n 5- ver itens da mochila \n"))

    if opcao == 1:
        item =input("add um item meu chapa : \n")
        mochila.append(item)
    elif opcao == 2 :
        item = input("qual item c quer tirar ? \n")
        if item in mochila:
            mochila.remove(item)
            print(f"vc tirou {item} da bag")
        else:
            print("esse item não tá na mochila")
    elif opcao == 3:
        item = input("qual item c quer modificar meu mn ? \n")
        if item in mochila:
            juncao = input("qual item c vai trocar ? \n")
            mochila[mochila.index(item)] = juncao
            print(f"vc trocou {item} por {juncao}")
        else:
            print("esse item não tá na mochila")
    elif opcao == 4:
        print("fechar mochila")
    elif opcao == 5 :
        print("esses são os itens q tu tem disponivel", mochila)