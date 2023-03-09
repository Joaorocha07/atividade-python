import modComissao, modMensagem
# from RHTDS import modDados

nome = input("\nDigite seu nome: ")
salario = float(input("Digite seu salario: "))
transformar = int(input("Voce quer transformar os números em real? (1 - Sim / 2 - Não) "))

while salario < 0:
    modMensagem.mensagem_erro(f"NÚMERO {salario} INVALIDO")
    salario = float(input("Digite seu salario: "))

if salario > 5000:
    modComissao.comissao30(salario, transformar, nome)

elif salario < 1000:
    modComissao.comissao200(salario, transformar, nome)

elif salario >= 3500 and salario <= 5000:
    modComissao.comissao70(salario, transformar, nome)

elif 1000 <= salario < 3500:
    modComissao.comissao50(salario, transformar, nome)