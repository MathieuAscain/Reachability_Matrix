import os

""" 
	Calculation of the closure matrix :
	Each 'ones' on the closure matrix comes from :
		- the transitive matrix previously calculated in the script transitive.py
		- the circuits which means a path can be found starting from a node and coming back to the same node
		For example starting to node A and finding a path to come back to node A 
"""

def closed(save, trans):
	# terminal clear
	os.system('cls' if os.name == 'nt' else 'clear')

	H = 2
	L = 6

	for i in range(len(save)):
		for j in range(len(save[i])):
			if i == j or trans[i][j] > 1 or save[i][j] == 1:
				trans[i][j] = 1

	for i in range(len(save)):
		for j in range(len(save[i])):
			print(f"\033[({i * H + 1}; {j * L + 1}H{save[i][j]}")

	for i in range(len(trans)):
		for j in range(len(trans[i])):
			print(f"\033[({len(trans) * H + H + 1 + i * H}; {j * L + 1}H{trans[i][j]}")

	print(f"\033[({len(trans) * H + H + 1 + i * H + 1};{j * L + 1}H")