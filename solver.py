import heapq
from utilities import swap_index

class C_State:
	def __init__(self, array, string, parent, f_coast):
		self.array = array
		self.string = string
		self.parent = parent
		self.f_coast = f_coast

def g(n): # the coast from starting pos to n
	val = 0
	return val

def h(arr, goal, heuristic_type): # heuristic: estimate the coast from the n pos to the tatget
	if heuristic_type == 1:
		return heuristic_func1(arr, goal)
	if heuristic_type == 2:
		return hamming(arr, goal)
	return manhattan_distance(arr, goal)

def heuristic_func1(arr, goal):
	return manhattan_distance(arr, goal)

def hamming(arr, goal):
	count = 0
	for i in range(len(goal)):
		if(arr[i] != goal[i]):
			count += 1
	return count

def manhattan_distance(array, goal):
	arr = array[:]
	count = 0
	for i in range(len(goal)):
		if (arr[i] != goal[i]):
			index = arr.index(goal[i])
			swap_index(arr, i, index)
			count += 1
	return count

def f(state, goal, heuristic_type):
	return g(state.parent.g) + h(state.arr, goal, heuristic_type)

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
