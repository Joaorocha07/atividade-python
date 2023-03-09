import random, os, time, joao
limparTela = lambda: os.system("cls")
limparTela()

def jogo_craps():
    dado = random.randint(2, 12)
    print("Primeira jogada:", dado)
    print()
    if dado == 7 or dado == 11:
        time.sleep(3.0)
        joao.mensagem_certo("Natural! Você ganhou!")
        print()
        return
    elif dado == 2 or dado == 3 or dado == 12:
        time.sleep(3.0)
        joao.mensagem_erro("Craps! Você perdeu.")
        print()
        return
    else:
        ponto = dado
        time.sleep(3.0)
        print(f"Seu Ponto é", ponto)
        print()
        while True:
            dado = random.randint(2, 12)
            print("Próxima jogada:", dado)
            time.sleep(1.8)
            if dado == ponto:
                time.sleep(3.0)
                joao.mensagem_certo("Você tirou seu Ponto novamente. Você ganhou!")
                print()
                return
            elif dado == 7:
                time.sleep(3.0)
                joao.mensagem_erro("Você tirou 7 antes de tirar seu Ponto novamente. Você perdeu.")
                print()
                return

jogo_craps()        