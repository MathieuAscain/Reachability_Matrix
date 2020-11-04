import os
from copy import deepcopy
from multiplication import multiple

class Error(Exception):
	""" Base class for other exceptions """
	pass

class NegativeNumber(Error):
	""" Raised when path length number is negative """
	pass

class NullLength(Error):
	""" Raised when the path length is null """


""" 
	Calculation of the transitive matrix :
	Each 'ones' on the matrix means :
		- a node has a successor reading lines
		- a node has a predecessor reading columns
"""

def transition(matrix):
	# terminal clear
	os.system('cls' if os.name == 'nt' else 'clear')

	# cursor position in console in function number of error messages
	cursor_position_in_console = 1

	# initialization of space in between coefficients in matrix (length and height)
	L = 6
	H = 2

	# initialization of a list for the recursive multiplication to find the final matrix
	result = []

	print("Dans la seconde fonction", matrix)

	while True:
		try:
			length_path = int(input("Select the path length = "))
			cursor_position_in_console += 1
			if length_path < 0:
				raise NegativeNumber
			elif length_path == 0:
				raise NullLength
			else:
				break
		except ValueError:
			print("Enter an integer")
			cursor_position_in_console += 1
		except NegativeNumber:
			print("The path length shall be strictly positive")
			cursor_position_in_console += 1
		except NullLength:
			print("The path length should not be null")
			cursor_position_in_console += 1

	print("\n")

	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			print(f"\033[({i * H + 3 + cursor_position_in_console};{j * L + 3}H{matrix[i][j]}")

	result = deepcopy(matrix)

	for i in range(length_path-1):
		result = deepcopy(multiple(matrix, result))

	for i in range(len(result)):
		for j in range(len(result[i])):
			print(f"\033[({len(matrix) * H + 3 + cursor_position_in_console + i * H + 1};{j * L + 3}H{result[i][j]}")

	print(f"\033[({len(matrix) * H + 3 + cursor_position_in_console + i * H + 2};{j * L + 3}H")

	return result

