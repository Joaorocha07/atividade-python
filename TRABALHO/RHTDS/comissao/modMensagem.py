import os, time

limparTela = lambda: os.system("cls")
limparTela()

def mensagem_erro(msg):
    limparTela()
    time.sleep(1.5)
    print()
    print("\033[1;49;31m-\033[m"*35)
    print(f"\033[1;49;31m{msg}\033[m")
    print("\033[1;49;31m-\033[m"*35)

def mensagem_certo(msg):
    limparTela()
    time.sleep(1.5)
    print()
    print("\033[1;49;32m-\033[m"*35)
    print(f"\033[1;49;32m{msg}\033[m")
    print("\033[1;49;32m-\033[m"*35)

def demonstrativo(salario, resComissao, resTotal, nome):
    limparTela()
    time.sleep(2.0)
    print()
    print(f"\033[0;49;34m+------------------------+----------------------+\033[m")
    print(f"\033[0;49;34m|\033[m Faixa de salário       \033[0;49;34m|\033[m Comissão             \033[0;49;34m|\033[m")
    print(f"\033[0;49;34m+------------------------+----------------------+\033[m")
    print(f"\033[0;49;34m| \033[mNome do funcionario    \033[0;49;34m|\033[m \033[1;49;32m{nome}\033[m              \033[0;49;34m|\033[m" )
    print(f"\033[0;49;34m|\033[m Seu salario            \033[0;49;34m|\033[m \033[1;49;32m{salario}\033[m          \033[0;49;34m|\033[m")
    print(f"\033[0;49;34m|\033[m Sua comissão           \033[0;49;34m|\033[m \033[1;49;32m{resComissao}\033[m            \033[0;49;34m|\033[m")
    print(f"\033[0;49;34m| \033[mValor total            \033[0;49;34m|\033[m \033[1;49;32m{resTotal}\033[m          \033[0;49;34m|\033[m" )
    print(f"\033[0;49;34m+------------------------+----------------------+\033[m")
    print()