import modMensagem, locale

def real(salario, resComissao, resTotal, transformar, nome):
    while transformar != 1 and transformar != 2 or salario < 0:
        modMensagem.mensagem_erro(f"VALOR {transformar} INVALIDO")
        transformar = int(input("Voce quer transformar os números em real? (1 - Sim / 2 - Não) "))
    if transformar == 1:
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        valorSalario = locale.currency(salario, grouping=True)
        valorComissao = locale.currency(resComissao, grouping=True)
        valorTotal = locale.currency(resTotal, grouping=True)
        modMensagem.demonstrativo(valorSalario, valorComissao, valorTotal, nome)
    elif transformar == 2:
        modMensagem.demonstrativo(salario, resComissao, resTotal, nome)

def comissao30(salario, transformar, nome):
    resComissao = 30 / 100 * 500
    resTotal = resComissao + salario
    real(salario, resComissao, resTotal, transformar, nome)

def comissao200(salario, transformar, nome):
    resComissao = 500 * 2 
    resTotal = resComissao + salario
    real(salario, resComissao, resTotal, transformar, nome)


def comissao70(salario, transformar, nome):
    resComissao = 70 / 100 * 500
    resTotal = resComissao + salario
    real(salario, resComissao, resTotal, transformar, nome)

def comissao50(salario, transformar, nome):
    resComissao = 500 - 250
    resTotal = resComissao + salario
    real(salario, resComissao, resTotal, transformar, nome)
