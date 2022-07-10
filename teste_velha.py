from velha import run

def testRightLength():
  matrixTest = [(0,0,0),(0,0,0),(0,0,0)]
  assert run(matrixTest) != "Tamanho incorreto" 

def testWrongLength():
  matrixTest = [(0,0,0),(0,0,0)]
  assert run(matrixTest) == "Tamanho incorreto" 

def testRightValue():
  matrixTest = [(2,0,1),(0,2,1),(0,2,0)]
  assert run(matrixTest) != "Valor incorreto" 

def testWrongValue():
  matrixTest = [(2,0,1),(6,2,1),(0,2,0)]
  assert run(matrixTest) == "Valor incorreto" 