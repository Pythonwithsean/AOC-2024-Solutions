from Helper import parseFile
from functools import cmp_to_key


rank = parseFile("./rank.txt")[0]
rank = [x.split("|") for x in rank]
rankMap = dict()
for person, before in rank: 
	if int(person) not in rankMap: 
		rankMap[int(person)] = [int(before)]
	else: 
		rankMap[int(person)].append(int(before))
updates = parseFile("./input.txt")[0]


def valid(key, v): 
	if int(key) not in rankMap:
		return True
	for person in rankMap[int(key)]: 
		if person in v: 
			return False
	return True

def part1(): 
	total = 0
	updateList = [x.split(",") for x in updates]
	for l in updateList: 
		v = True
		visited = set()
		for person in l: 
			if not valid(person, visited):
				v = False
				break 
			else:
				visited.add(int(person))
		if v: 
			total += int(l[len(l) // 2])
	print(total)
				



# Bubble sort to validate the list
def validateList(line): 
	N = len(line)
	for i in range(N - 1): 
		for j in range(len(line) - 1): 
			first, second = line[j], line[j + 1]
			if int(first) in rankMap[int(second)]: 
				line[j], line[j + 1] = line[j + 1], line[j]
	return line


def part2(): 
	total = 0
	updateList = [x.split(",") for x in updates]
	for i in range(len(updateList)): 
		v = True
		visited = set()
		sort = False
		for k in range(len(updateList[i])): 
			canPlace = valid(updateList[i][k], visited)
			if not canPlace:
				v = False
			else:
				visited.add(int(updateList[i][k]))	
		if not v:
			total += int(validateList(updateList[i])[len(updateList[i]) // 2])
	print(total)	

part2()