################   print   #####################

def print_puzle(arr, size):
	print (size)
	for y in range(size):
		for x in range(size):
			print ("%s" % str(arr[x + y * size]), end="\t")
		print("")

################   solve   #####################

def solve_puzzle(start, goal, size):
	print("solving puzzle")
	print_puzle(start, size)
	print("\t  ||\n\t  ||\n\t  \\/")
	print_puzle(goal, size)
	return False
