from heapq import heappush, heappop
from utilities import *

################   classes   #####################

class C_State:
	def __init__(self, array, string, parent, level, cost):
		self.array = array
		self.string = string
		self.parent = parent
		self.cost = cost
		self.level = level

	def __lt__(self, nxt):
		return self.cost < nxt.cost

	def __eq__(self, other):
		return self.string == other.string

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

################ cost functions #####################

# the cost from starting pos to n (depth cost)
def g(level):
	return level + 1

# heuristic: estimate the cost from the n pos to the tatget
def h(arr, goal, size, heuristic_type = 0) -> int:
	if heuristic_type == 1:
		return my_heuristic(arr, goal, size)
	if heuristic_type == 2:
		return hamming(arr, goal, size)
	if heuristic_type == 3:
		return manhattan_hamming(arr, goal, size)
	if heuristic_type == 4:
		return random_web(arr, goal, size)
	if heuristic_type == 5:
		return number_of_swaps(arr, goal, size)
	if heuristic_type == 6:
		return linear_conflicts(arr, goal, size)
	return manhattan_distance(arr, goal, size)

################   heuristics   #####################

def my_heuristic(arr, goal, s) -> int:
	count = 0
	for i in range (s * s):
		if (arr[i] != goal[i]):
			index = arr.index(goal[i])
			count += abs(index - i)
	return count

def manhattan_hamming(arr, goal, s) -> int:
	return hamming(arr, goal, s) + manhattan_distance(arr, goal, s)

def hamming(arr, goal, s) -> int:
	count = 0
	for i in range(s * s):
		if(arr[i] != goal[i]):
			count += 1
	return count

def number_of_swaps(array, goal, s) -> int:
	arr = array[:]
	count = 0
	for i in range(s * s):
		if (arr[i] != goal[i]):
			index = arr.index(goal[i])
			swap_index(arr, i, index)
			count += 1
	return count

def random_web(array, goal, s) -> int:# impliment new method here
	return hamming(array, goal, s) + my_heuristic(array, goal, s)

#manhatn distance
def manhattan_distance(array, goal, s) -> int:
	count = 0
	for i in range(s * s):
		if (array[i] != 0 and array[i] != goal[i]):
			index = array.index(goal[i])
			count += get_parity(i, index, s)
	return count

def linear_conflicts(array, goal, size):
	def get_row_col(arr, s):# % col, / row
		row = [-1 for i in range(s * s)]
		col = [-1 for i in range(s * s)]
		for i in range (s * s):
			element = arr[i]
			row[element] = int(i / s)
			col[element] = i % s
		return row, col

	def linear_c(arr, goal, s):
		g_row , g_col = get_row_col(goal, s)
		row, col = get_row_col(arr, s)
		count = 0
		for i in range(1, s * s):
			if (g_row[i] == row[i]):
				r = g_row[i]
				for j in range(i + 1, s * s):
					if (row[j] == r and row[j] == g_row[j]):
						if (g_col[i] < g_col[j] and col[i] > col[j]):
							count += 1
		return count * 2

	return linear_c(array, goal, size) + manhattan_distance(array, goal, size)

def f(level, arr, goal, size, s_method, heuristic_type = 0) -> int:
	if (s_method == 2) :
		return h(arr, goal, size, heuristic_type)
	if (s_method == 3) :
		return g(level)
	return g(level) + h(arr, goal, size, heuristic_type)

################   print   #####################
def prRed(skk):
	print("\033[91m {}\033[00m" .format(skk), end="")

def print_puzle(arr, size, Debug=False):
	#print (size)
	for y in range(size):
		for x in range(size):
			if(Debug):prRed ("%s" % str(arr[x + y * size]))
			else:print("%s" % str(arr[x + y * size]), end="")
		print("")

################   solve   #####################

def solve_puzzle(start, goal, size, search_method, heuristic_type):
	print("","solving puzzle")
	print_puzle(start, size)
	print("\t  ||\n\t  ||\n\t  \\/")
	search(start, goal, size, heuristic_type, search_method)
	#print_puzle(goal, size)
	return False

def get_childs(state, size, goal, heuristic_type, s_method):
	#Cstate: array, string, parent, level, cost
	lst = []
	index_0 = state.array.index(0)
	if (can_move_up(index_0,size)):
		arr = state.array.copy()
		swap_index(arr, index_0, index_0 - size)
		cost = f(state.level, arr, goal, size, s_method, heuristic_type)
		new_state = C_State(arr, array_to_str(arr),state, state.level + 1, cost)
		lst.append(new_state)
	if (can_move_down(index_0,size)):
		arr = state.array.copy()
		swap_index(arr, index_0, index_0 + size)
		cost = f(state.level, arr, goal, size, s_method, heuristic_type)
		new_state = C_State(arr, array_to_str(arr),state, state.level + 1, cost)
		lst.append(new_state)
	if (can_move_left(index_0,size)):
		arr = state.array.copy()
		swap_index(arr, index_0, index_0 - 1)
		cost = f(state.level, arr, goal, size, s_method, heuristic_type)
		new_state = C_State(arr, array_to_str(arr),state, state.level + 1, cost)
		lst.append(new_state)
	if (can_move_right(index_0,size)):
		arr = state.array.copy()
		swap_index(arr, index_0, index_0 + 1)
		cost = f(state.level, arr, goal, size, s_method, heuristic_type)
		new_state = C_State(arr, array_to_str(arr),state, state.level + 1, cost)
		lst.append(new_state)
	return (lst)

def is_value_in_list(value, lst):
	for x in lst:
		if(x.string == value.string):
			return x, True
	return None, False

def print_path(state, size):
	path_list = []
	node = state
	while (node.level != 0):
		path_list.append(node.array)
		node = node.parent
	path_list.append(node.array)
	path_list.reverse()
	for x in path_list:
		print_puzle(x, size, False)
		print("")

def search(start, goal, size, heuristic_type, search_method):
	goal_str = array_to_str(goal)
	opened = priority_queue()
	closed = []
	iterations = -1
	root = C_State(start, array_to_str(start), None, 0, h(start, goal, size, heuristic_type))
	opened.push(root)
	success = False
	while (opened.empty() == False) and (success == False):
		iterations += 1
		min_state = opened.pop()
		if (min_state.string == goal_str):
			success = True
			print_path(min_state, size)
			print("heap:",len(opened.heap))
			print("closed", len(closed))
			print("iteration:", iterations)
			print("path len", min_state.level)
			break
		else:
			closed.append(min_state)
			childs = get_childs(min_state, size, goal, heuristic_type, search_method)
			for child in childs:
				child_in_closed, closed_bool = is_value_in_list(child, closed)
				child_in_opened, opened_bool = is_value_in_list(child, opened.heap)
				#if (child not in opened.heap) and (child_in_closed == None):
				if (opened_bool == False) and (closed_bool == False):
					opened.push(child)
				else:# s is in 'opened' or in 'closed'
					if (closed_bool == True) and (child_in_closed.level > child.level):
						closed.remove(child_in_closed)
						opened.push(child)
					elif (opened_bool == True) and (child_in_opened.level > child.level):
						child_in_opened.parent = min_state
						child_in_opened.level = child.level
						child_in_opened.cost = child.cost

	if (success == True):
		print("---*-*-*-*-*-*-*-* puzzle solved *-*-*-*-*-*-*-*---")
	else:
		print("---*-*-* i can t solve this puzzle, i m too weak *-*-*---")


# understanf generat_goal
# add hash for closed states (set ?)
# fromat output
# add tile-corner and last-tile heuristics
# pThread ?
# -> push
