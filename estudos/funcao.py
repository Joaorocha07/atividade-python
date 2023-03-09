import os, time
limparTela = lambda: os.system("cls")
limparTela()

def mensagem(msg):
    print("\033[1;49;31m-\033[m"*35)
    print(msg)
    print("\033[1;49;32m-\033[m"*35)
    print()
mensagem("MENSAGEM")
time.sleep(2.4)


def soma(a,b):
    soma_dos_valores = a + b
    mensagem(f"A sua soma é \033[1;49;32m{soma_dos_valores}\033[m")
soma(10,20)
time.sleep(2.4)

def contador(*num):
    tamanho = len(num)
    mensagem(f"Os valores \033[1;49;32m{num}\033[m, o tamanho é \033[1;49;32m{tamanho}\033[m")
contador(10,20)
time.sleep(2.4)


def soma_valores(*valores):
    soma = 0
    for num in valores:
        soma += num
    mensagem(f"A soma dos valores: \033[1;49;32m{valores}\033[m é igual a soma \033[1;49;32m{soma}\033[m")
soma_valores(10,23,23,12)


time.sleep(2.4)
nome = input("Qual é o seu nome?")
mensagem(f"SEU NOME É {nome.upper()}")
print()