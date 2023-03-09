import os, time, joao
limparTela = lambda: os.system("cls")
limparTela()

def somaImposto(taxaImposto, Custo):
    while taxaImposto < 0 or Custo < 0:
        limparTela()
        joao.mensagem_erro(f"         VALOR INVALIDO") 
        print()
        taxaImposto = float(input('Digite a taxa de imposto: '))
        Custo = float(input('Digite o custo: '))
    return (1 + taxaImposto/100)*Custo

joao.mensagem_certo("      CALCULADOR DE IMPOSTO")
print()
taxa = float(input('Digite a taxa de imposto: '))
custo = float(input('Digite o custo: '))
print()
time.sleep(1.5)
print("\033[1;49;32m-\033[m"*35)
print("Valor com imposto:", somaImposto(taxa,custo))
print("\033[1;49;32m-\033[m"*35)
print()