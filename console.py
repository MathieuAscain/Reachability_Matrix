from new_matrix import user_selection
from transitive import transition
from closure import closed
from copy import deepcopy

choice = 'A'
save = []
trans = []

print("\n")
while choice != 'Q' and choice != 'q':
	print("Selection of a new matrix ................. 1")
	print("p length path matrix ...................... 2")
	print("Transitive closure ........................ 3")
	print("Quit ...................................... Q")
	print("\n")
	choice = input("Make your choice baby ! ")

	if choice == '1':
		save = deepcopy(user_selection())
		print(save)
	elif choice == '2':
		trans = deepcopy(transition(save))
	elif choice == '3':
		closed(save, trans)



