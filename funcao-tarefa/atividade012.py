import os, time, joao
from random import shuffle
limparTela = lambda: os.system("cls")
limparTela()

def embaralha(nome):
    a = list(nome)
    shuffle(a)
    a = ''.join(a)
    print(a.lower())

joao.mensagem_certo("O PROGRAMA IRÁ MOSTRAR SEU NOME EMBARALHADO")
print()
nome = input('Digite seu nome: ')
time.sleep(2.0)
print()
embaralha(nome)
print()