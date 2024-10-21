import numpy as np

matrix = np.array([[1, 2], [4, 5]])
matrix1 = np.array([[1, 3], [5, 6]])

shape=matrix.shape # -> (2,3), 2 rows and 3 columns
dimentions=matrix.ndim # -> 2 dimentions 

# Accessing
first_second=matrix[0][1] #-> 2
both_first_elms=matrix[:,0] #-> [1 4]

# manipulate
scaled=matrix*2 #-> [[2,4,6],[8,10,12]]
matrix_multiply=np.dot(matrix,matrix1) #-> raise error if .shape != r,c, where r==c
another_matrix_multiply=matrix@matrix1 #-> same as np.dot

transposed_mtx=matrix.T #-> [[1,4],[2,5]]

inverse_matrix = np.linalg.inv(matrix) #-> inverse of the matrix

# Determinant of the matrix
det = np.linalg.det(matrix)

identity_matrix = np.eye(3) #[[1. 0. 0.],[0. 1. 0.],[0. 0. 1.]]

sliced_mtx=matrix[:,:2] #-> Slicing matrix to get the two first columns

zero_matrix = np.zeros((2, 3)) #-> [[0,0,0],[0,0,0]]
ones_matrix = np.ones((3, 2)) #-> np.ones((rows, columns))

