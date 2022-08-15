import numpy as np;


def matrixElimination(matrixA,matrixB):
  a = np.matrix(matrixA)
  b = np.matrix(matrixB)

  b = b.transpose()
  a = a.I;
  
  return a*b
  
  
a = [[4,-1],[7,-13]]
b = [18,504]



print(matrixElimination(a,b));

# v1 = -6, v2 = -42
