import os, time, joao
limparTela = lambda: os.system("cls")
limparTela()

def soma3(a, b, c):
    while a < 0 or b < 0 or c < 0:
        if a < 0:
            limparTela()
            time.sleep(1.5)
            joao.mensagem_erro(f"VALOR INVALIDO {a}")
        if b < 0:
            limparTela()
            time.sleep(1.5)
            joao.mensagem_erro(f"VALOR INVALIDO {b}")
        if c < 0:
            limparTela()
            time.sleep(1.5)
            joao.mensagem_erro(f"VALOR INVALIDO {c}")

        a = int(input("Primeiro número: "))
        b = int(input("Segundo número: "))
        c = int(input("Terceiro número: "))
        limparTela()
    s = a + b + c
    return s

joao.mensagem_certo("SOMA DE TRÊS NÚMEROS")
print()
a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))
print()
limparTela()
time.sleep(1.5)
joao.mensagem_certo(f"Resultado: {soma3(a,b,c)}")