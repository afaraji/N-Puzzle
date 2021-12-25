from heapq import heappush, heappop
from utilities import swap_index

class C_State:
	def __init__(self, array, string, parent, level, cost):
		self.array = array
		self.string = string
		self.parent = parent
		self.cost = cost
		self.level = level
	def __lt__(self, nxt):
		return self.cost < nxt.cost

class priority_queue:
	def __init__(self):
		self.heap = []

	# Inserts a new key 'k'
	def push(self, k):
		heappush(self.heap, k)

	# Method to remove minimum element
	# from Priority Queue
	def pop(self):
		return heappop(self.heap)

	# Method to know if the Queue is empty
	def empty(self):
		if not self.heap:
			return True
		else:
			return False

def g(level): # the cost from starting pos to n
	return level + 1

def h(arr, goal, heuristic_type) -> int: # heuristic: estimate the cost from the n pos to the tatget
	if heuristic_type == 1:
		return my_heuristic(arr, goal)
	if heuristic_type == 2:
		return hamming(arr, goal)
	return manhattan_distance(arr, goal)


def my_heuristic(arr, goal) -> int:
	count = 0
	for i in range (len(goal)):
		if (arr[i] != goal[i]):
			index = arr.index(goal[i])
			count += abs(index - i)
	return count

def hamming(arr, goal) -> int:
	count = 0
	for i in range(len(goal)):
		if(arr[i] != goal[i]):
			count += 1
	return count

def manhattan_distance(array, goal) -> int:
	arr = array[:]
	count = 0
	for i in range(len(goal)):
		if (arr[i] != goal[i]):
			index = arr.index(goal[i])
			swap_index(arr, i, index)
			count += 1
	return count

def f(state, goal, heuristic_type) -> int:
	return g(state.parent.level) + h(state.arr, goal, heuristic_type)

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
