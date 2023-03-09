import os
limparTela = lambda: os.system("cls")
limparTela()

lista = []

def compra(saldo, valor):
    if saldo >= valor:
        saldo -= valor # -> diminui o saldo pelo valor que a pessoa colocou
        return saldo, True
    else:
        return saldo, False

def media(lista):
    soma = 0
    media = 0
    cont = 0
    for valor in lista:
        cont += 1
        soma += valor["valor"]
    media = soma / cont
    print("\033[1;49;32m-\033[m"*37)
    print(f"Média dos valores comprados \033[1;49;32mR$ {media}\033[m")
    print("\033[1;49;32m-\033[m"*37)

def menu(saldo):
    while True:
        print("\033[1;49;32m\n---------------MENU---------------\033[m")
        print("[1] -> VER SALDO")
        print("[2] -> FAZER COMPRA")
        print("[3] -> MÉDIA DOS PRODUTOS COMPRADOS")
        print("[4] -> Sair")
        print("\033[1;49;32m-\033[m"*33)
        opcao = input("")
        limparTela()

        if opcao == "1":
            limparTela()
            print("\033[1;49;32m-\033[m"*18)
            print(f"Saldo: R$ \033[1;49;32m{saldo}\033[m")
            print("\033[1;49;32m-\033[m"*18)

        elif opcao == "2":
            limparTela()
            valor = float(input("\nValor da compra: R$"))
            while valor < 0:
                 limparTela()
                 print("\033[1;49;31m-\033[m"*22)
                 print(f"NÚMERO \033[1;49;31m{valor}\033[m INVÁLIDO!")
                 print("\033[1;49;31m-\033[m"*22)
                 #CONCERTAR ERRO -> contabilizar número invalido
                 valor = float(input("\nValor da compra: R$"))
            produto = input("Produto comprado: ")

            #Chamando a função compra
            saldo, sucesso = compra(saldo, valor)
            dicionario = {"valor":valor, "produto": produto}

            lista.append(dicionario)

            #SE TIVER O SALDO SUFICIENTE
            if sucesso:
                limparTela()
                print(f"\033[1;49;32mCOMPRA NO VALOR DE R$ {valor} EFETUADO COM SUCESSO!\033[m")
                print("\033[1;49;32m-\033[m"*25)
                print(f"Item comprado {produto}")
                print(f"Novo saldo \033[1;49;32mR$ {saldo}\033[m")
                print("\033[1;49;32m-\033[m"*25)

            #SE NÃO TIVER O SALDO SUFICIENTE
            else:
                limparTela()
                print("\033[1;49;31m-\033[m"*20)
                print("\033[1;49;31mSALDO INSUFICIENTE!\033[m")
                print("\033[1;49;31m-\033[m"*20)

        # MÉDIA DOS PRODUTOS
        elif opcao == "3":

            if not lista:
                print("\033[1;49;31m-\033[m"*28)
                print("\033[1;49;31mNEMNHUMA COMPRA REALIZADA!\033[m")
                print("\033[1;49;31m-\033[m"*28)
                
            else:
                media(lista)
            #print("AINDA NÃO TA FUNCIONANDO A MEDIA!")

        # SAIR    
        elif opcao == "4":
            limparTela()
            print("\033[1;49;31m-\033[m"*20)
            print("\033[1;49;31mPROGRAMA ENCERRADO!\033[m")
            print("\033[1;49;31m-\033[m"*20)
            print()
            break
        else:
            print("\033[1;49;31m-\033[m"*15)
            print("\033[1;49;31mOPÇÃO INVALIDA\033[m")
            print("\033[1;49;31m-\033[m"*15)

saldo_inicial = float(input("\nSaldo inicial: R$"))
while saldo_inicial < 0:
    limparTela()
    print("\033[1;49;31m-\033[m"*22)
    print(f"NÚMERO \033[1;49;31m{saldo_inicial}\033[m INVÁLIDO!")
    print("\033[1;49;31m-\033[m"*22)
    saldo_inicial = float(input("\nSaldo inicial: R$"))

limparTela() 
menu(saldo_inicial)