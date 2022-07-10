from velha import run

def testLengthRight():
  matrixTest = [(0,0,0),(0,0,0),(0,0,0)]
  assert run(matrixTest) != "Tamanho incorreto" 

def testLengthWrong():
  matrixTest = [(0,0,0),(0,0,0)]
  assert run(matrixTest) == "Tamanho incorreto" 

def testValueRight():
  matrixTest = [(2,0,1),(0,2,1),(0,2,0)]
  assert run(matrixTest) != "Valor incorreto" 

def testValueWrong():
  matrixTest = [(2,0,1),(6,2,1),(0,2,0)]
  assert run(matrixTest) == "Valor incorreto" 