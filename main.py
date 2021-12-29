import sys
import argparse
import time
from utilities import *
from solver import *

############## read input #################

def read_input_file(file):
	try:
		f = open(file,'r')
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
		print("Error while handeling file:", "'" + file + "'")
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

############## TERMINAL ANIMATION #################

def text_animation(string) :
	for x in string:
		print('\33[33m' + x, end='')
		sys.stdout.flush()
		time.sleep(0.03)
	time.sleep(1)
	print('\033[0m')

############## main #################
if __name__ == "__main__":
	
	#help usage and errors are automatically generated when there is invalid arguments
	parser = argparse.ArgumentParser()

	parser.add_argument("-s", type=int, default=1, help="Search methode to solve the puzzle")
	parser.add_argument("-f", type=int, default=7, help="Type of heuristic function to solve the puzzle")
	parser.add_argument("-l", action='store_true', help="Get list of search methodes and heuristic types to solve puzzle")
	parser.add_argument('filename', nargs='?')

	args = parser.parse_args()

	#----- Usage for s and f arguments ------#
	if args.s < 1 or args.s > 3:
		print ("You must insert 1 or 2 or 3")
		sys.exit(1)

	if args.f < 1 or args.f > 7:
		print ("You must insert a number between 1 & 7")
		sys.exit(1)

	
	search_method = args.s
	heuristic_type = args.f

	#----- Get l flag input ------#
	if (args.filename) and (args.l) :
		print("Please select a search methode to solve the puzzle")
		print("1 - A* (defalut)")
		print("2 - Greedy search")
		print("3 - Uniform-cost")
		search_method = int(input("Enter number here :"))
		print("Please select a heuristic to solve the puzzle")
		print("1 - my_heuristic")
		print("2 - hamming")
		print("3 - manhattan_hamming")
		print("4 - random 1")
		print("5 - random 2")
		print("6 - linear_conflicts")
		print("7 - manhattan_distance (defalut)")
		heuristic_type = int(input("Enter number here :"))

	#----- Get search_method args ------#

	if (args.filename) :
		if (search_method == 1):
			text_animation("\n************************ A* (defalut) **************************")
		elif (search_method == 2):
			text_animation("\n*********************** Greedy search **************************")
		else :
			text_animation("\n************************ Uniform-cost **************************")

	#----- Get heuristic_type args ------#

	if (args.filename) :
		if (heuristic_type == 1):
			text_animation("*************** Heuristic type : MY_HEURISTIC  *****************")
		elif (heuristic_type == 2):
			text_animation("****************** Heuristic type : HAMMING  *******************")
		elif (heuristic_type == 3):
			text_animation("*********** Heuristic type : MANHATTAN & HAMMING  **************")
		elif (heuristic_type == 4):
			text_animation("****************** Heuristic type : RANDOM1  *******************")
		elif (heuristic_type == 5):
			text_animation("***************** Heuristic type : RANDOM12  *******************")
		elif (heuristic_type == 6):
			text_animation("************* Heuristic type : LINEAR_CONFLICTS  ***************")
		elif (heuristic_type == 7):
			text_animation("******** Heuristic type : MANHATTAN_DISTANCE 'default' *********")
		
	#----- Open and read filename / Usage ------#
	if args.filename:
		size, arr_2D, arr_1D = read_input_file(args.filename)
	else:
		parser.print_usage()
		sys.exit(1)

	goal = generate_final_state(size)
	if (is_solvable(arr_1D[:], goal,size)):
		tic = time.time()
		solve_puzzle(arr_1D, goal, size, search_method, heuristic_type)
		elapsed = round(time.time() - tic, 5)
		print("puzzle solved in:", str(elapsed * 1000), "ms")
	else: print("The puzzle is unsolvable.")



# heapq
