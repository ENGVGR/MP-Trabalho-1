"""
Tests to function in velha.py
"""

from velha import run

def test_right_length():
  matrix_test = [(0,0,0),(0,0,0),(0,0,0)]
  assert run(matrix_test) != "Tamanho incorreto"

def test_wrong_length():
  matrix_test = [(0,0,0),(0,0,0)]
  assert run(matrix_test) == "Tamanho incorreto"

def test_right_value():
  matrix_test = [(2,0,1),(0,2,1),(0,2,0)]
  assert run(matrix_test) != "Valor incorreto"

def test_wrong_value():
  matrix_test = [(2,0,1),(6,2,1),(0,2,0)]
  assert run(matrix_test) == "Valor incorreto"

def test_not_undefined():
  matrix_test = [(2,0,1),(2,0,0),(2,1,0)]
  assert run(matrix_test) != "Resultado indefinido"

def test_is_undefined():
  matrix_test = [(2,0,1),(0,0,0),(0,2,0)]
  assert run(matrix_test) == "Resultado indefinido"
  matrix_test = [(2,0,1),(2,0,0),(2,1,0)]
  assert run(matrix_test) == "Resultado indefinido"
