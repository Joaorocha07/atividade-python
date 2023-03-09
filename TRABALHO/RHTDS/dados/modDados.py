def formatoReal(dado):
    dado = input("Insira um dado: ")


def formatoReal(valor_str):
    try:
        # Tentar converter a string para float
        valor = float(valor_str.replace(',', '.'))
        # Se a conversão for bem-sucedida, retornar o valor como float
        return valor
    except ValueError:
        # Se a conversão não for bem-sucedida, exibir uma mensagem de erro
        print("Valor monetário inválido. Por favor, informe um valor válido.")
        return None

valor = input("Informe o valor monetário: ")
valor_formatado = formatoReal(valor)

if valor_formatado:
    print("Valor informado: R$ {:.2f}".format(valor_formatado))

