def lengthWrong(matrix):
    if (len(matrix) != 3 or len(matrix[0]) != 3 or len(matrix[1]) != 3 or len(matrix[2]) != 3):
        return True
    else:
        return False

def run(matrix):
    if (lengthWrong(matrix)):
        erro = "Tamanho incorreto"
        return erro
    else: 
        return 0