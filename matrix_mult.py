import numpy as np

A = np.array([[1, 4,7,10],
              [2,5,8,None],
              [None,6,9,12],
              [None,None,None,None]])

B = np.array([[1, 2, None,7,8,9],
              [4,5,6,10,None,12]])

np.dot(A,B)