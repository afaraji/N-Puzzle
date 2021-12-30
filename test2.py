

#					 = liner| manhattn  | total
#[0,2,1,7,4,5,6,3,8] = 2	| 6			| 8
#[0,2,1,5,4,3,6,7,8] = 6	| 6			| 12	*
#[4,3,6,8,0,7,5,2,1] = 0	| 22		| 22
#[2,7,0,5,4,3,8,1,6] = 10	| 14		| 24	*
#goal:012345678


#array = [7,0,15,14,6,4,2,3,13,12,8,1,9,5,11,10]
#goal = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
array =[2,7,0,\
		4,5,3,\
		8,1,6]

goal = [1,2,3,\
		4,5,6,\
		7,8,0]
size = 3



def corner_corner(arr, goal, s):
	count = 0
	if goal[0] != 0 and goal[0] != arr[0]:
		if goal[1] == arr[1]:count += 2
		if goal[s] == arr[s]:count += 2
	if goal[s - 1] != 0 and goal[s - 1] != arr[s - 1]:
		if goal[s - 2] == arr[s - 2]: count += 2
		if goal[2 * s - 1] == arr[2 * s - 1]: count += 2
	if goal[s * s - 1] != 0 and goal[s * s - 1] != arr[s * s - 1]:
		if goal[s * s - 1 - s] == arr[s * s - 1 - s]: count += 2
		if goal[s * s - 2] == arr[s * s - 2]: count += 2
	if goal[s * s - s] != 0 and goal[s * s - s] != arr[s * s - s]:
		if goal[s * s - s - s] == arr[s * s - s - s]: count += 2
		if goal[s * s - s + 1] == arr[s * s - s + 1]: count += 2
	return count


print (corner_corner(array, goal, size))
