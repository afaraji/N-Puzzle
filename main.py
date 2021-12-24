import sys
from utilities import *
from solver import *

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
		for i in range(1, size + 1):
			tmp = data[i].split()
			tmp = [int(i) for i in tmp]
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

if __name__ == "__main__":
	size, arr_2D, arr_1D = read_input_file()
	goal = generate_final_state(size)
	if (is_solvable(arr_1D[:], goal,size)):
		solve_puzzle(arr_1D, goal, size)
	else: print("The puzzle is unsolvable.")


# heapq
