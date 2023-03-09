import os, time, joao
limparTela = lambda: os.system("cls")
limparTela()

def converta(hora, minuto):
    if 0 < hora <= 11 and 0 <= minuto < 60:
        print()
        time.sleep(1.0)
        joao.mensagem_certo(f'SUA CONVERSÃO  -> {hora}:{minuto} AM')
        print()
        print("O PROGRAMA IRÁ REINICIAR")
        time.sleep(3.0)
        limparTela()
    
    elif hora == 0  and 0 <= minuto < 60:
        print()
        time.sleep(1.0)
        joao.mensagem_certo(f'SUA CONVERSÃO  -> {hora + 12}:{minuto} AM')
        print()
        print("O PROGRAMA IRÁ REINICIAR")
        time.sleep(3.0)
        limparTela()

    elif 12 == hora and 0 <= minuto <= 60:
        print()
        time.sleep(1.0)
        joao.mensagem_certo(f'SUA CONVERSÃO  -> {hora}:{minuto} PM')
        print()
        print("O PROGRAMA IRÁ REINICIAR")
        time.sleep(3.0)
        limparTela()

    elif 12 <= hora < 24 and 0 <= minuto < 60:
        print()
        time.sleep(1.0)
        joao.mensagem_certo(f'SUA CONVERSÃO  -> {hora - 12}:{minuto} PM')
        print()
        print("O PROGRAMA IRÁ REINICIAR")
        time.sleep(3.0)
        limparTela()

    else:
        print()
        joao.mensagem_erro('VALOR INVALIDO!')
        time.sleep(3.0)
        limparTela()

while True:
    joao.mensagem_certo("       CONVERTOR DE HORA")
    print()
    hora = int(input('Hora: '))
    if hora == 999: 
        limparTela()
        joao.mensagem_certo("PROGRAMA ENCERRADO")
        break
    minuto = int(input('Minuto: '))
    converta(hora,minuto)
    print()

# AM -> MANHÃ
# PM -> TARDE