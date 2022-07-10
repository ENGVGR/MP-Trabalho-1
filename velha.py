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

def impossible(matrix):
  amount_x = cont_values(matrix, 1)
  amount_circle = cont_values(matrix, 2)
  if amount_x > amount_circle:
    return amount_x > amount_circle + 1
  elif amount_x < amount_circle:
    return amount_x + 1 < amount_circle
  else:
    return False

def horizontal_winner(matrix):
  for i in range(3):
    if (matrix[i][0] == matrix[i][1] and matrix[i][1] == matrix[i][2]
    and matrix[i][0] != 0):
      return matrix[i][0]
  return False

def vertical_winner(matrix):
  for i in range(3):
    if (matrix[0][i] == matrix[1][i] and matrix[1][i] == matrix[2][i]
    and matrix[0][i] != 0):
      return matrix[0][i]
  return False

def cross_winner(matrix):
  if (matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2]
  and matrix[0][0] != 0):
    return matrix[0][0]
  return False

def result(matrix):
  h_winner = horizontal_winner(matrix)
  v_winner = vertical_winner(matrix)
  c_winner = cross_winner(matrix)

  if h_winner:
    return h_winner
  if v_winner:
    return v_winner
  if c_winner:
    return c_winner
  else:
    return 0

def undefined(matrix):
  return (0 in matrix[0] or 0 in matrix[1] or 0 in matrix[2])

def run(matrix):
  if wrong_length(matrix):
    erro = "Tamanho incorreto"
    return erro
  if wrong_value(matrix):
    erro = "Valor incorreto"
    return erro
  if impossible(matrix):
    erro = -2
    return erro
  else:
    if (result(matrix) == 0 and undefined(matrix)):
      return -1
    else:
      return result(matrix)
