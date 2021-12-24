import argparse
from os import truncate
import sys

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


# return 0 if they r on the same row/col
# positive: start is above/after goal by (returned value)
# negative: start is below/before goal by (returned value)

def get_parity(s_index, g_index, size):
	same_row = int(s_index / size) - int(g_index/ size)
	same_col = (s_index % size) - (g_index % size)
	num_of_moves = abs(same_row) + abs(same_col)
	return num_of_moves % 2

def is_solvable(start_state, goal_state, size):
	parity = get_parity(start_state.index(0), goal_state.index(0), size)
	count = 0
	for i in range(len(start_state)):
		if (start_state[i] != goal_state[i]):
			index_to_swap_with = start_state.index(goal_state[i])
			swap_index(start_state, i, index_to_swap_with)
			count += 1
	print("num of swaps:", count)
	if(count % 2 == parity):
		return True
	return False

def generate_final_state(s):
	ts = s*s
	puzzle = [-1 for i in range(ts)]
	cur = 1
	x = 0
	ix = 1
	y = 0
	iy = 0
	while True:
		puzzle[x + y*s] = cur
		if cur == 0:
			break
		cur += 1
		if x + ix == s or x + ix < 0 or (ix != 0 and puzzle[x + ix + y*s] != -1):
			iy = ix
			ix = 0
		elif y + iy == s or y + iy < 0 or (iy != 0 and puzzle[x + (y+iy)*s] != -1):
			ix = -iy
			iy = 0
		x += ix
		y += iy
		if cur == s*s:
			cur = 0

	return puzzle

################   print   #####################

def print_puzle(arr, size):
	print (size)
	for y in range(size):
		for x in range(size):
			print ("%s" % str(arr[x + y * size]), end="\t")
		print("")

################ movement #####################

def swap_index(arr, i, j):
	#print(arr, "swaping:", i, "and",j)
	tmp = arr[i]
	arr[i] = arr[j]
	arr[j] = tmp
	return arr

def swap_values(arr, a, b):# not used yet
	a_index = arr.index(a)
	b_index = arr.index(b)
	arr[a_index] = b
	arr[b_index] = a
	return arr

# to move down:		newPos = pos + size		\ only if: newPos < size * size
# to move up:		newPos	= pos - size	\ only if: newPos >= 0
# to move left:		newPos = pos - 1		\ only if: pos mode size != 0
# to move right:	newPos = pos + 1		\ only if: newPos mode size != 0

def can_move_left(i, s):
	if (i % s != 0):
		return True
	return False

def can_move_right(i, s):
	if (i + 1) % s != 0:
		return True
	return False

def can_move_up(i, s):
	if (i - s >= 0):
		return True
	return False

def can_move_down(i, s):
	if (i + s < s * s):
		True
	return False

def move_left():
	return False

def move_right():
	return False

def move_up():
	return False

def move_down():
	return False

############## read input #################

def read_input_file():
	if len(sys.argv) != 2:
		print("python3 nPuszzle.py puzzle.txt")
		exit(1)
	try:
		f = open(sys.argv[1],'r')
		lines = f.readlines()
		f.close()
		count = 0
		data = []
		for line in lines:
			count += 1
			line = line.strip()
			try: hashtag = line.index("#")
			except: hashtag = -1
			if (hashtag != -1): line = line[:hashtag]
			if (len(line) > 0): data.append(line)
	except:
		print("Error while handeling file:", "'" + sys.argv[1] + "'")
		exit(2)
	arr = []
	m_ap = []
	try:
		size = int(data[0])
		check_replicat = range(size * size)
		for i in range(1, size + 1):
			tmp = data[i].split()

			tmp = [int(i) for i in tmp] #still need to check if i (th elemnts in tmp) is in check_replicat
			m_ap.append(tmp)
			arr += tmp
			if (len(m_ap[-1]) != size):
				raise Exception()
		if (len(m_ap) != size):
			raise Exception()
		# need to verify if no number is replicated
		return size, m_ap, arr
	except:
		print("Invalid File.")
		exit(3)

############## main #################
def solve_puzzle(start, goal, size):
	print("solving puzzle")
	print_puzle(start, size)
	print("\t\t||\n\t\t||\n\t\t\\/")
	print_puzle(goal, size)
	return False

if __name__ == "__main__":
	size, arr_2D, arr_1D = read_input_file()
	goal = generate_final_state(size)
	if (is_solvable(arr_1D[:], goal,size)):
		solve_puzzle(arr_1D, goal, size)
	else: print("The puzzle is unsolvable.")


# heapq
