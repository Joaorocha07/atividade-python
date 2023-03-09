num = 0
lista = []
while num < 3:
    nome_produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    print()
    cadastro = {"nome do produto": nome_produto, "preço do produto": preco}
    lista.append(cadastro)
    num += 1

print("--------PRODUTOS--------")
for i in lista:
    
    for chave, valor in i.items():
        print(chave, valor)
    print()