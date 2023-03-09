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
    for i in range(0, valor):
        for cont in range(i + 1):
            print(cont + 1, end=" ")
        print()
        time.sleep(1.10)
    joao.mensagem_certo("PROGRAMA ENCERRADO")
       

contador()
