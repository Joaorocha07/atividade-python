import os, time, joao
limparTela = lambda: os.system("cls")
limparTela()

def reverso(n):
    return str(n[::-1])

print()
n = str(input('Digite um número: ')).strip()
print()
time.sleep(2.0)
joao.mensagem_certo(f'Reverso: {reverso(n)}')
print()