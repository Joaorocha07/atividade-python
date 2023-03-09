import random, os, time
limparTela = lambda: os.system("cls")
limparTela()

def mensagem_erro(msg):
    print("\033[1;49;31m-\033[m"*35)
    print(f"\033[1;49;31m{msg}\033[m")
    print("\033[1;49;31m-\033[m"*35)

def mensagem_certo(msg):
    print("\033[1;49;32m-\033[m"*35)
    print(f"\033[1;49;32m{msg}\033[m")
    print("\033[1;49;32m-\033[m"*35)

# Define as opções de aposta
opcoes_cor = ["vermelho", "preto", "verde"]

# Define a lista de números da roleta
numeros_roleta = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]

# Define o saldo inicial
saldo = 100

# Define a variável de execução
executando = True

# Inicia o loop principal do jogo
while executando:

    # Pergunta ao usuário qual opção de aposta deseja escolher
    print("\nOpções de aposta: vermelho, preto, verde")
    print()
    cor_aposta = input("Escolha a cor que deseja apostar: ")

    # Verifica se a aposta é válida
    if cor_aposta not in opcoes_cor:
        mensagem_erro("Aposta inválida, escolha vermelho, preto ou verde")
        continue

    # Pergunta ao usuário qual valor deseja apostar
    valor_aposta = float(input("Quanto deseja apostar? Saldo atual: R$" + str(saldo) + " "))
    limparTela()
    # Verifica se o usuário tem saldo suficiente
    if valor_aposta > saldo:
        mensagem_erro("Saldo insuficiente.")
        continue

    # Gera um número aleatório para a roleta
    numero_sorteado = numeros_roleta[random.randint(0, len(numeros_roleta) - 1)]

    # Verifica se a cor apostada é igual a cor do número sorteado
    cor_sorteada = "vermelho" if numero_sorteado in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36] else "preto" if numero_sorteado in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35] else "verde"

    if cor_aposta == cor_sorteada:
        time.sleep(2.4)
        print()
        mensagem_certo(f"Cor sorteada {cor_sorteada}")
        print()
        mensagem_certo("Parabéns! você ganhou R$" + str(valor_aposta) + "!")
        saldo += valor_aposta
    else:
        time.sleep(2.4)
        print()
        mensagem_erro("Você errou!")
