import os, time, joao
limparTela = lambda: os.system("cls")
limparTela()

def valorPagamento(prestacao, d):
    return prestacao*1.03 + 0.001*d

c = total = 0

while True:
    joao.mensagem_certo("DIGITE 0 PARA VER O RESULTADO")
    print()
    prestacao = float(input('Valor da prestação: '))
    while prestacao < 0:
        time.sleep(2.0)
        limparTela()
        joao.mensagem_erro("          VALOR INVALIDO")
        print()
        prestacao = float(input('Valor da prestação: '))
        
    if prestacao == 0:
        time.sleep(2.0)
        limparTela()
        joao.mensagem_certo(f'Total: {total}\nQuantidade: {c} ')
        print()
        break
    d = int(input('Dia em atraso: '))
    print(f'Valor a ser pago: {valorPagamento(prestacao, d) :.2f}')
    print('-'*25)
    c += 1
    total += valorPagamento(prestacao, d)
    time.sleep(2.5)
    limparTela()