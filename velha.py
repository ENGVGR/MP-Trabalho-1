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

def cont_values(matrix, value):
  return (matrix[0].count(value) + matrix[1].count(value)
    + matrix[2].count(value))

def undefined(matrix):
  amount_x = cont_values(matrix, 1)
  amount_circle = cont_values(matrix, 2)
  if amount_x > amount_circle:
    return amount_x > amount_circle + 1
  elif amount_x < amount_circle:
    return amount_x + 1 < amount_circle
  else:
    return False

def run(matrix):
  if wrong_length(matrix):
    erro = "Tamanho incorreto"
    return erro
  if wrong_value(matrix):
    erro = "Valor incorreto"
    return erro
  if undefined(matrix):
    erro = -1
    return erro
  else:
    return 0
