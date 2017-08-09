import sys

matrix_1 = [[8, 4, 5, 5, 0], [7, 10, 0, 10, 10], [1, 10, 3, 6, 1]]
matrix_2 = [[2, 6, 6], [0, 10, 2], [4, 1, 8]]
matrix_3 = [[5, 0, 10], [10, 0, 6], [10, 3, 2], [9, 3, 5], [0, 5, 8]]

def multiplyMat(mat1, mat2):
	if len(mat1) != len(mat2[0]):
		print("error")
		return []
	
	new_mat = []
	
	for i in range(len(mat2)):
		new_mat.append([])
		for j in range(len(mat1[0])):
			scalar = 0
			for x in range(len(mat1)):
				scalar += mat1[x][j] * mat2[i][x]
			
			new_mat[i].append(scalar)
	
	return new_mat

ar = multiplyMat(matrix_2,matrix_3)
print(ar)