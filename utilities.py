
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
	def incriment(i, j, _m):
		return i + _m[0], j + _m[1]

	def change_mode(_m):
		# (row, col)
		# > : v | > (0,1)
		# v : < | v (1,0)
		# < : ^ | < (0,-1)
		# ^ : > | ^ (-1,0)

		if _m == (0,1):return (1,0)
		if _m == (1,0):return (0,-1)
		if _m == (0,-1):return (-1,0)
		return (0,1)

	g = [i for i in range(1, s*s)]
	g.append(0)
	g_index = 0
	m = [[-1 for i in range(s)] for j in range(s)]
	i = j = 0
	mode = (0,1)
	while g_index < s * s:
		if i < 0 or j < 0 or i == s or j == s or m[i][j] != -1:
			i -= mode[0]
			j -= mode[1]
			mode = change_mode(mode)
			i,j = incriment(i, j, mode)
		else:
			m[i][j] = g[g_index]
			i,j = incriment(i, j, mode)
			g_index += 1
	arr = []
	for x in m:
		arr += x
	return arr


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
