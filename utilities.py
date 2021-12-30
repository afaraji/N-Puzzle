
# return 0 if they r on the same row/col
# positive: start is above/after goal by (returned value)
# negative: start is below/before goal by (returned value)

def get_parity(s_index, g_index, size):
	same_row = int(s_index / size) - int(g_index/ size)
	same_col = (s_index % size) - (g_index % size)
	num_of_moves = abs(same_row) + abs(same_col)
	return num_of_moves

def is_solvable(start_state, goal_state, size):
	try:
		parity = get_parity(start_state.index(0), goal_state.index(0), size)
	except:
		print("Error: '0' not found. incorrect puzzle format")
		exit(6)
	count = 0
	for i in range(size * size):
		if (start_state[i] != goal_state[i]):
			try:
				index_to_swap_with = start_state.index(goal_state[i])
			except:
				print("Error: '" + str(goal_state[i]) + "' not found. incorrect puzzle format")
				exit(7)
			swap_index(start_state, i, index_to_swap_with)
			count += 1
	if(count % 2 == parity % 2):
		return True
	return False

def array_to_str(arr):
	return ''.join(map(str, arr))

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
		return True
	return False
