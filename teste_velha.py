from velha import run

def testLengthRight():
  matrixTest = [(0,0,0),(0,0,0),(0,0,0)]
  assert run(matrixTest) != "Tamanho incorreto" 

def testLengthWrong():
  matrixTest = [(0,0,0),(0,0,0)]
  assert run(matrixTest) == "Tamanho incorreto" 
