def wrongLength(matrix):
    if (len(matrix) != 3 or len(matrix[0]) != 3 or len(matrix[1]) != 3 or len(matrix[2]) != 3):
        return True
    else:
        return False

def wrongValue(matrix):
    correctValues = [0,1,2]
    for line in matrix:
        for value in line:
            if (value not in correctValues):
                return True
    return False

def run(matrix):
    if (wrongLength(matrix)):
        erro = "Tamanho incorreto"
        return erro
    if (wrongValue(matrix)):
        erro = "Valor incorreto"
        return erro
    else: 
        return 0