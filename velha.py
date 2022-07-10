"""
Functions to run a tic-tac-toe.
"""

def wrong_length(matrix):
  return (len(matrix) != 3 or len(matrix[0]) != 3 or len(matrix[1]) != 3
    or len(matrix[2]) != 3)

def wrong_value(matrix):
  correct_values = [0,1,2]
  for line in matrix:
    for value in line:
      if value not in correct_values:
        return True
  return False

def run(matrix):
  if wrong_length(matrix):
    erro = "Tamanho incorreto"
    return erro
  if wrong_value(matrix):
    erro = "Valor incorreto"
    return erro
  else:
    return 0
