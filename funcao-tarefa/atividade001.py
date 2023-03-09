import os, time, joao
limparTela = lambda: os.system("cls")
limparTela()

def contador():
    valor = int(input("Digite um valor: "))
    
    while valor < 0 or valor > 10 or valor == 0:
        limparTela()
        joao.mensagem_erro(f"VALOR {valor} INVALIDO ")
        valor = int(input("Digite um valor: "))

    limparTela()
    print()
    joao.mensagem_certo("O PROGAMA VAI COMEÇAR A RODAR!")    
    for cont in range(1, valor + 1):
        print(f"{cont} " * cont)
        time.sleep(1.10)
    joao.mensagem_certo("PROGRAMA ENCERRADO")
       
contador()
