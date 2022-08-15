import numpy as np;


def matrixElimination(matrixA,matrixB):
  a = np.matrix(matrixA)
  b = np.matrix(matrixB)

  b = b.transpose()
  a = a.I;
  
  return a*b
  
  
a = [[3,-2,-1],[-4,7,-1],[2,-3,1]]
b = [12,0,0]



print(matrixElimination(a,b));
