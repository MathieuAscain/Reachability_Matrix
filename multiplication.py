""" 
	Matrix multiplication :
		- to the power of the path length selected by user in the script transitive.py

"""

def multiple(matrix, result):
	recursive = [[0] * len(matrix) for _ in range(len(matrix))]
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			final_coef = 0
			for k in range(len(matrix)):
				coef = 0
				coef = matrix[i][k] * result[k][j]
				final_coef = coef + final_coef
			recursive[i][j] = final_coef
	return recursive


