
corrida = {}
cont = 1
cont_v = 1
voltas = []

while cont < 2:
    nome = input(f"Digite o nome do corredor {cont}: ")
    cont +=1
    
while cont_v < 10:
    tempo = float(input(f"Digite o tempo da volta {cont_v} em segundos: "))
    cont_v +=1
    voltas.append(tempo)
    cont_v += 1
    corrida[nome] = voltas
    cont += 1
    melhor_volta = []
for nome in corrida:
    voltas = corrida[nome]
    melhor = voltas[0]
for volta in voltas:
    if melhor > volta:
        melhor = volta
        melhor_volta.append([nome, melhor])
        print(f' A melhor volta de: {melhor_volta}')