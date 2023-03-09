import os, time, joao
limparTela = lambda: os.system("cls")
limparTela()

def inteiros(n):
    return len((str(n)))

n = str(input('Digite um número: ')).strip()
print()
time.sleep(2.0)
joao.mensagem_certo(f'Esse número tem {inteiros(n)} dígitos')
print()