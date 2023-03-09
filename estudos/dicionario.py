import os
limparTela = lambda: os.system("cls")
limparTela()

pessoas_cadastradas = []
total_cadastro = int(input('\nQuantas pessoas quer cadastrar: '))

while total_cadastro > 0:
    nome = (input('\nDigite seu nome: '))
    idade = int(input('Digite a sua idade: '))
    cadastro = {"nome": nome, "idade": idade}
    pessoas_cadastradas.append(cadastro)
    limparTela()
    total_cadastro -= 1

for i in pessoas_cadastradas:
    for chave, valor in i.items():
        print(f"{chave} {valor}")
    print()
        