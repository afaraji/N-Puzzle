import sys
import time
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
		data = []
		for line in lines:
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
			if (len(tmp) != size):
				raise Exception()
			m_ap.append(tmp)
			arr += tmp
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
		tic = time.time()
		solve_puzzle(arr_1D, goal, size)
		elapsed = round(time.time() - tic, 5)
		print("puzzle solved in:", str(elapsed * 1000), "ms")
	else: print("The puzzle is unsolvable.")


# heapq
