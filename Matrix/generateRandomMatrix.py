import sys
import random

def generateRandomMatrix():
	return 1
	

n_row = 3
n_col = 5
range_min = 0
range_max = 10

matrix = []

for i in range(n_col):
	matrix.append([])
	for j in range(n_row):
		matrix[i].append(random.randint(range_min, range_max))

print(matrix)
	