import heapq

def g(n): # the coast from starting pos to n
	val = 0
	return val

def h(n, heuristic): # heuristic: estimate the coast from the n pos to the tatget
	if heuristic == 1:
		return manhattan_distance(n)
	if heuristic == 2:
		return manhattan_distance(n)
	return manhattan_distance(n)

def heuristic_func1(n):
	return manhattan_distance(n)

def heuristic_func2(n):
	return manhattan_distance(n)

def manhattan_distance(n):
	return 0

def f(n):
	return g(n) + h(n)

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
