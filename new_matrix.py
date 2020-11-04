
import os

class Error(Exception):
	""" Base class for other exceptions """
	pass

class NegativeNumber(Error):
	""" Raised when number is negative """
	pass

class HigherNumber(Error):
	""" Raised when nodes number is higher than 5 """
	pass

"""
	Matrix selection
	Maximum size limited to 5 rows/columns

"""
def user_selection():
	# initialization of number of nodes to enter in while loop
	nodes = 6

	# initialization of space in between coefficients in matrix (length and height)
	L = 6
	H = 2

	# cursor position in console in function number of error messages
	cursor_position_in_console = 1

	# terminal clear
	os.system('cls' if os.name == 'nt' else 'clear')

	# nodes number selection
	while True:
		try:
			nodes = int(input("Enter the number of nodes. Max 5 = "))
			cursor_position_in_console += 1
			if nodes <= 0:
				raise NegativeNumber
			elif nodes > 5:
				raise HigherNumber
			else:
				break
		except ValueError:
			print("Enter an integer")
			cursor_position_in_console += 1
		except NegativeNumber:
			print("The number of nodes shall be strictly positive")
			cursor_position_in_console += 1
		except HigherNumber:
			print("The number of nodes should not be higher 5")
			cursor_position_in_console += 1

	print("Adjacency matrix selection (0 or 1) ")

	# initialization of the adjacency matrix
	M = [[0] * nodes for _ in range(nodes)]

	# show a dot at each position where a coefficient shall be selected
	for i in range(len(M)):
		for j in range(len(M[i])):
			print(f"\033[({i * H + 3 + cursor_position_in_console}; {j * L + 1}H.")

	# User coefficient selection
	for i in range(len(M)):
		for j in range(len(M[i])):
			M[i][j] = int(input(f"\033[({i * H + 3 + cursor_position_in_console}; {j * L + 1}H"))

	print("\n")

	return M



