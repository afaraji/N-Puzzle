import argparse
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

def is_solvable(start_state, goal_state):
	start_state = [1,2,3,4,5,6,7,8,0]
	goal_state = [1,2,3,4,5,6,7,8,0]
	return False

################ movement #####################

def swap_index(arr, i, j):
	tmp = arr[i]
	arr[i] = arr[j]
	arr[j] = tmp
	return arr

def swap_values(arr, a, b):
	a_index = arr.index(a)
	b_index = arr.index(b)
	arr[a_index] = b
	arr[b_index] = a
	return arr

def can_move_left():
	return False

def can_move_right():
	return False

def can_move_up():
	return False

def can_move_down():
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
		exit(2)

############## main #################

if __name__ == "__main__":
	size, arr_2D, arr_1D = read_input_file()


# heapq
