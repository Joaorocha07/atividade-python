import random
import time

import os
limparTela = lambda: os.system("cls")
limparTela()


# Variáveis iniciais
money = 100  # dinheiro inicial do jogador
play = True  # indicador se o jogo está em execução

while play:
    # Exibir mensagem de boas-vindas e regras do jogo
    print("Bem-vindo ao jogo do tempo!")
    print("Regras:")
    print("- Você tem", money, "de dinheiro.")
    print("- Você pode apostar ou não.")
    print("- Se você apostar e acertar o número de segundos, seu dinheiro será dobrado.")
    print("- Se você apostar e errar o número de segundos, você perderá todo o dinheiro apostado.")
    print("- O jogo será pausado por 10 segundos entre as partidas.")
    limparTela()

    # Aceitar entrada do usuário para apostar ou não
    bet = input("Você deseja apostar? (s/n) ")
    if bet == "s":
        # Aceitar entrada do valor da aposta
        bet_amount = int(input("Quanto deseja apostar? "))
        if bet_amount > money:
            limparTela()
            print("Você não tem dinheiro suficiente para essa aposta.")
            continue
        money -= bet_amount

        # Gerar número aleatório de segundos
        seconds = random.randint(1, 10)

        # Exibe o tempo aleatório
        print("O tempo é: ", seconds)
        
        # Aceitar entrada do usuário para o número de segundos
        guess = int(input("Em quantos segundos você acha que é o tempo? "))

        # Verificar se o usuário acertou o número de segundos
        if guess == seconds:
            print("Parabéns, você acertou!")
            money += bet_amount * seconds
        else:
            print("Você errou. O tempo é", seconds, "segundos.")
            print("Você perdeu", bet_amount, "de dinheiro.")
    else:
        # Gerar número aleatório de segundos para o foguete parar
        seconds = random.randint(1, 10)

        # Exibe o tempo aleatório
        print("O tempo é: ", seconds)

    # Pausar o jogo por 10 segundos
    time.sleep(10)
