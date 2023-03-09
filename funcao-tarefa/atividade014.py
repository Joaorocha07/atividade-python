def is_magic_square(square):
    # verifica se a soma das linhas é igual
    row_sum = sum(square[0])
    for i in range(1, len(square)):
        if sum(square[i]) != row_sum:
            return False
    
    # verifica se a soma das colunas é igual
    for i in range(len(square)):
        col_sum = 0
        for j in range(len(square)):
            col_sum += square[j][i]
        if col_sum != row_sum:
            return False
    
    # verifica se a soma da diagonal principal é igual
    diag_sum = 0
    for i in range(len(square)):
        diag_sum += square[i][i]
    if diag_sum != row_sum:
        return False
    
    # verifica se a soma da diagonal secundária é igual
    diag_sum = 0
    for i in range(len(square)):
        diag_sum += square[i][len(square) - i - 1]
    if diag_sum != row_sum:
        return False
    
    return True

def find_magic_squares():
    # gera todas as combinações de números de 1 a 9
    import itertools
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    squares = list(itertools.permutations(numbers, 9))
    
    # divide as combinações em sublists de 3 elementos
    squares = [square[i:i+3] for square in squares for i in range(0, len(square), 3)]
    
    # divide as sublists em matrizes 3x3
    squares = [square[i:i+3] for square in squares for i in range(0, len(square), 3)]
    
    # verifica se a matriz é um quadrado mágico
    magic_squares = [square for square in squares if is_magic_square(square)]
    
    # mostra os quadrados mágicos encontrados
    for square in magic_squares:
        print(square)

find_magic_squares()
