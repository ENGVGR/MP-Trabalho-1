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

def horizontal_winner(matrix, value):
  for i in range(len(matrix)):
    if (matrix[i][0] == matrix[i][1] and matrix[i][1] == matrix[i][2]
    and matrix[i][0] == value):
      return 1
  return False

def vertical_winner(matrix, value):
  for i in range(len(matrix)):
    if (matrix[0][i] == matrix[1][i] and matrix[1][i] == matrix[2][i]
    and matrix[0][i] == value):
      return 1
  return False

def cross_winner(matrix, value):
  if (matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2]
  and matrix[0][0] == value):
    return 1
  return False

def result(matrix):
  h_winner_x = horizontal_winner(matrix, 1)
  h_winner_circle = horizontal_winner(matrix, 2)
  v_winner_x = vertical_winner(matrix, 1)
  v_winner_circle = vertical_winner(matrix, 2)
  c_winner_x = cross_winner(matrix, 1)
  c_winner_circle = cross_winner(matrix, 2)

  amount_winners = (h_winner_x + h_winner_circle + v_winner_x + v_winner_circle
    + c_winner_x + c_winner_circle)

  if amount_winners > 1:
    return -2

  if h_winner_x:
    return 1
  elif h_winner_circle:
    return 2
  elif v_winner_x:
    return 1
  elif v_winner_circle:
    return 2
  elif c_winner_x:
    return 1
  elif c_winner_circle:
    return 2
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
