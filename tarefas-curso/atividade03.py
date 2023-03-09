import os
limparTela = lambda: os.system("cls")
limparTela()

lista = []
num = 1
media = 0
soma = 0

for num in range(1,5):
    notas = float(input(f"{num}° Nota: "))
    
    while notas < 0 or notas > 10:
        limparTela()
        print("\033[1;49;91m-\033[m"*20)
        print(f"NOTA \033[1;49;91m{notas}\033[m INVALIDA")
        print("INSIRA NOVAMENTE")
        print("\033[1;49;91m-\033[m"*20)
        print()
        notas = float(input(f"{num}° Nota: "))

    soma += notas
    lista.append({"notas":notas})
media = soma / 4
limparTela()
     
print("\033[1;49;32m--------SUAS NOTAS--------\033[m")
cont = 0
for i in lista:
    cont +=1
    for chave, valor in i.items():
        print(cont, chave,valor)
print("\033[1;49;32m-\033[m"*26)
print()
print("\033[1;49;32m--------SUA MÉDIA--------\033[m")
print(f"Sua média é {media}")
print("\033[1;49;32m-\033[m"*26)
print()