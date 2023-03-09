import os, time
limparTela = lambda: os.system("cls")
limparTela()

def ret(largura, altura):
    if largura > 20:
        largura = 20
    if altura > 20:
        altura = 20
    time.sleep(0.5)
    print('\033[1;49;31m-+-\033[m' * largura)
    c =0
    while c < altura:
        time.sleep(0.5)
        z = '|'
        print(f'\033[1;49;32m{z}{z:>{(largura*3 - 1)}}\033[m')
        c += 1
    time.sleep(0.5)
    print('\033[1;49;31m-+-\033[m' * largura)

print()
largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))
print()
time.sleep(1.8)
ret(largura, altura)
print()