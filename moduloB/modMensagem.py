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

def demonstrativo(salario, resComissao, resTotal):
    limparTela()
    time.sleep(2.0)
    print()
    print(f"+------------------------+----------------------+")
    print(f"| Faixa de salário       | Comissão             |")
    print(f"+------------------------+----------------------+")
    print(f"| Seu salario            | {salario}          |")
    print(f"| Sua comissão           | {resComissao}            |")
    print(f"| Valor total            | {resTotal}          |" )
    print(f"+------------------------+----------------------+")
    print()