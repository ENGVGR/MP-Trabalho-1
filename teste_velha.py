import velha

def test_length_right():
  matrixTest = [(0,0,0),(0,0,0),(0,0,0)]
  assert run(matrixTest) != "Tamanho incorreto" 

def test_length_wrong():
  matrixTest = [(0,0,0),(0,0,0)]
  assert run(matrixTest) == "Tamanho incorreto" 
