from Helper import parseFile

inp = parseFile("./input.txt")[0]
inp = [list(x) for x in inp]


def getGuardPos():
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            if inp[i][j] in "^>v<":
                inp[i][j] = "X"
                return i, j
	
def getNextDir(dir):
	if dir == "up":
		return "right"
	if dir == "right":
		return "down"
	if dir == "down":
		return "left"
	if dir == "left":
		return "up"
		
def getMove(dir): 
	if dir == "up":
		return (-1,0)
	if dir == "right":
		return (0,1)
	if dir == "down": 
		return (1,0)
	if dir == "left":
		return (0,-1)

def part1():
    N, M = len(inp), len(inp[0])
    x,y =  getGuardPos()
    direction = "up"
    visited = set()
    visited.add((x,y))
    while 0 <= x < N and 0 <= y < M:	
        dx,dy = getMove(direction)
        nx,ny = x + dx, y + dy
        if nx in range(0, N) and ny in range(0, M) and inp[nx][ny] == "#":
            direction = getNextDir(direction)
        else:
            x,y = nx, ny
            if 0 <= x < N and 0 <= y < M:
                visited.add((x, y))
                inp[x][y] = "X"
    print(len(visited))


 

part1()
