import sys

matrix_1 = [[8, 4, 5, 5, 0], [7, 10, 0, 10, 10], [1, 10, 3, 6, 1]]
matrix_2 = [[2, 6, 6], [0, 10, 2], [4, 1, 8]]
matrix_3 = [[5, 0, 10], [10, 0, 6], [10, 3, 2], [9, 3, 5], [0, 5, 8]]

def transpose(mat):
	n_row = len(mat)
	n_col = len(mat[0])
	mat_transpose = []
	for i in range(n_col):
		mat_transpose.append([])
		for j in range(n_row):
			mat_transpose[i].append(mat[j][i])
	
	return mat_transpose
	
matrix = transpose(matrix_1)
print(str(matrix))