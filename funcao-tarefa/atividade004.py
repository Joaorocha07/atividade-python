import os, time, joao
limparTela = lambda: os.system("cls")
limparTela()

def verificador():
    joao.mensagem_certo('POSITIVO OU NEGATIVO')
    print()
    n = int(input('digite um número: '))
    if n > 0:
        time.sleep(1.10)
        print()
        joao.mensagem_certo(f"POSITIVO \nSeu número é {n}")
    elif n == 0:
        time.sleep(1.10)
        print()
        joao.mensagem_certo(f"NULO \nSeu número é {n}")
    elif n < 0:
        time.sleep(1.10)
        print()
        joao.mensagem_certo(f"NEGATIVO \nSeu número é {n}")

verificador()