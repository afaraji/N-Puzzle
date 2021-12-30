#!/usr/local/bin/python3

# import sys
# import time
# from heapq import heappush, heappop

# class priority_queue:
# 	def __init__(self):
# 		self.heap = []

# 	# Inserts a new key 'k'
# 	def push(self, k):
# 		heappush(self.heap, k)

# 	# Method to remove minimum element
# 	# from Priority Queue
# 	def pop(self):
# 		return heappop(self.heap)

# 	# Method to know if the Queue is empty
# 	def empty(self):
# 		if not self.heap:
# 			return True
# 		else:
# 			return False

# def read_input_file():
# 	if len(sys.argv) != 2:
# 		print("python3 nPuszzle.py puzzle.txt")
# 		exit(1)
# 	f = open(sys.argv[1],'r')
# 	lines = f.readlines()
# 	f.close()
# 	count = 0
# 	data = []
# 	for line in lines:
# 		count += 1
# 		line = line.strip()
# 		try: hashtag = line.index("#")
# 		except: hashtag = -1
# 		if (hashtag != -1): line = line[:hashtag]
# 		if (len(line) > 0): data.append(line)

# 	arr = []
# 	m_ap = []

# 	try:
# 		size = int(data[0])
# 		for i in range(1, size + 1):
# 			tmp = data[i].split()
# 			tmp = [int(i) for i in tmp]
# 			m_ap.append(tmp)
# 			arr += tmp
# 			if (len(m_ap[-1]) != size):
# 				raise Exception()
# 		if (len(m_ap) != size):
# 			raise Exception()
# 		return m_ap, arr
# 	except:
# 		print("Invalid File.")
# 		exit(2)

# myList, array = read_input_file()
# print(myList)
# print(array)

# class C_State:
# 	def __init__(self, array, string, parent, f_coast):
# 		self.array = array
# 		self.string = string
# 		self.parent = parent
# 		self.f_coast = f_coast
# 	def print(self):
# 		return self.array, self.string

# lol = C_State("123", "789", None, 100)

# print(lol)


# class test:
# 	def __init__(self, level, cost):
# 		self.cost = cost
# 		self.level = level
# 	def __lt__(self, nxt):
# 		return self.cost < nxt.cost

# 	def __eq__(self, other):
# 		return self.cost == other.cost



# lst = priority_queue()
# val1 = test(10, 5)
# val2 = test(12, 7)
# val3 = test(1, 3)
# val4 = test(20, 25)
# val5 = test(15, 2)

# lst.push(val1)
# lst.push(val2)
# lst.push(val3)
# lst.push(val4)
# lst.push(val5)

# new_val = test(13, 7)

# # for x in lst:
# # 	print(x)
# lst.heap.remove(new_val)
# print(new_val in lst.heap)
# print(new_val in lst.heap)

# import heapq

# class Element:
# 	def __init__(self, key, value):
# 		self.key = key
# 		self.value = value

# 	def __lt__(self, nxt):
# 		return self.key < nxt.key

# 	def __eq__(self, other):
# 		return self.key == other.key

# heap = []
# element1 = Element('A', 1)
# element2 = Element('B', 2)
# element3 = Element('C', 3)
# heapq.heappush(heap, element1)
# heapq.heappush(heap, element2)
# heapq.heappush(heap, element3)

# print( Element('A', 1) in heap )     # True
# print(Element('A', 100) in heap)    # True
# print(Element('D', 1) in heap)

import threading
import time


def print_cube(num):
	for i in range(num):
		for j in range(num):
			time.sleep(1)
			print("cube")

def print_square(num):
	for i in range(num):
		time.sleep(4)
		print("square")

if __name__ == "__main__":
	n = 3
	# creating thread
	t1 = threading.Thread(target=print_square, args=(n,), name="first")
	t2 = threading.Thread(target=print_cube, args=(n,), name="second")
	t1.daemon = True
	t2.daemon = True
	thrds = []
	thrds.append(t1)
	thrds.append(t2)
	t1.start()
	t2.start()
	done = False
	while not done:
		for x in thrds:
			if(x.is_alive() == False):
				print("--->", x.getName() , "is Done. EXITING")
				done = True
				break

	# both threads completely executed
	print("Done!")
