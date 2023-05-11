import itertools

def det_4x4(matrix):
    if len(matrix) != 4 or len(matrix[0]) != 4:
        raise ValueError("A matriz não é 4x4")
    indices = [0, 1, 2, 3]
    permuta = itertools.permutations(indices)
    det = 0
    for perm in permuta:
        sinal = 1
        for i in range(4):
            for j in range(i + 1, 4):
                if perm[i] > perm[j]:
                    sinal *= -1
        produto = 1
        for i in range(4):
            produto *= matrix[i][perm[i]]
        det += sinal * produto
    return det

# solicita ao usuário para digitar os elementos da matriz 4x4
matrix = []
for i in range(4):
    row = input(f"Digite os elementos da {i+1}ª linha separados por espaço: ")
    matrix.append([int(x) for x in row.split()])

# calcula a determinante usando a fórmula de Leibniz
det = det_4x4(matrix)

# imprime o resultado
print(f"A determinante da matriz é {det}.")