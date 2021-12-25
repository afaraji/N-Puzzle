import sys


# read = sys.stdin.readline().strip()
# print("----> " + read)
# read = sys.stdin.readline().strip()
# print("----> " + read)



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

class C_State:
	def __init__(self, array, string, parent, f_coast):
		self.array = array
		self.string = string
		self.parent = parent
		self.f_coast = f_coast
	def print(self):
		return self.array, self.string

lol = C_State("123", "789", None, 100)

print(lol)
