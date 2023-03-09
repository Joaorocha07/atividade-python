import os
limparTela = lambda: os.system("cls")
limparTela()

lista = []

for cont in range(1,5):
    item = input(f"Digite {cont}° itens: ")

    lista.append({
        'item':item
    })


posicao = int(input("Digite um número: "))

print(f"{lista[posicao]}")

