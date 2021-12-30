

# class C_State:
# 	def __init__(self, array, string, parent, level, cost):
# 		self.array = array
# 		self.string = string
# 		self.parent = parent
# 		self.cost = cost
# 		self.level = level

# 	def __lt__(self, nxt):
# 		return self.cost < nxt.cost

# 	def __eq__(self, other):
# 		return self.string == other.string

# 	def __hash__(self) -> int:
# 		return (int(self.string))


# closed = set()
# node1 = C_State([1,2,3,4], "1234", None, 0, 5)
# node2 = C_State([1,2,3,4], "1243", None, 1, 3)
# node3 = C_State([1,2,3,4], "2134", None, 2, 7)
# nodeX = C_State([1,2,3,4], "1243", None, 0, 5)
# closed.add(node1)
# closed.add(node2)
# closed.add(node3)

# lol = nodeX not in closed
# print(lol, len(closed))
# inmem = None
# for x in closed:
# 	if nodeX == x:
# 		inmem = x
# isItthus = closed.pop()
# print(hex(id(nodeX)), hex(id(node2)), hex(id(inmem)),hex(id(isItthus)))
# closed.remove(nodeX)
# lol = node2 not in closed
# print(lol, len(closed))

goal = [1,2,3,8,0,4,7,6,5] # s = 3
# goal = [1,2,3,4,12,13,14,5,11,0,15,6,10,9,8,7] # s = 4


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

def map_goal(s):
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
	while g_index < s*s:
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

for x in range(3,100):
	if generate_final_state(x) == map_goal(x):
		print("for %d\tresulte is CORRECT" %x)
	else:
		print("for %d ++++++++++++++++resulte is FALSE" %x)
exit(0)

size = int(input("enter size: "))
goal = generate_final_state(size)
print("goal   :",goal)
puzzle = map_goal(size)
print("puzzle :", puzzle)
print(puzzle == goal)
