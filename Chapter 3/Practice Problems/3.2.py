import numpy as np;


def matrixElimination(matrixA,matrixB):
  a = np.matrix(matrixA)
  b = np.matrix(matrixB)

  b = b.transpose()
  a = a.I;
  
  return a*b
  
  
a = [[5,-2,-3],[4,5,0],[3,-6,-4]]
b = [24,0,0]



print(matrixElimination(a,b));

# v1 = -32, v2 = -25.6, v3 = 62.4
