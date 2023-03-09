precos_produtos = {
    "Nootbook": 1500,
    "Pc Gamer": 3500,
    "Iphone": 4500,
    "Teste": "item removido"
}

# Proucurar um produto
celular = precos_produtos["Iphone"]
print(celular)
print()

# Adicionar um novo item
precos_produtos["Mouse"] = 200
print(precos_produtos)
print()


# Percorrendo as chave dentro do dicionario sem formatação
print(precos_produtos.keys())
print()

# Percorrendo as chave dentro do dicionario
for chave in precos_produtos:
    print(chave)
print()


# Todos os valores dentro do dicionario sem formatação
print(precos_produtos.values())
print()

# Procurando os valores dentro do dicionario
for chave in precos_produtos:
    print (precos_produtos[chave])
print()


# Todos os valores e chaves dentro do dicionario - sem formatação
print(precos_produtos.items())
print()

for chave, valor in precos_produtos.items():
    print(chave, valor)
print()


# Retirar um valor do dicionario
precos_produtos.pop("Teste")
print(precos_produtos)
print()

# Verificar se a chave existe dentro do dicionario ou não
if "Teste" in precos_produtos:
    print('---EXISTE---')
else:
    print('---NÃO EXISTE---')

# Verificar se o valor existe dentro do dicionario ou não
if "item removido" in precos_produtos.values():
    print('---EXISTE---')
else:
    print('---NÃO EXISTE---')

#Função enumerate(): serve para gerar uma chave numérica sequencial que pode ser associado a uma lista
lista = ["A", "B", "C", "D", "E", "F", "G"]

for i, letra in enumerate(lista):
    print(i + 10, letra)
    #print(i, letra)