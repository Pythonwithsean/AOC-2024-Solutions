from Helper import parseFile

inp = parseFile("./input.txt")[0]

directions = [
    (0, 1), 
    (1, 0), 
    (0, -1), 
    (-1, 0), 
    (1, 1),  
    (-1, -1), 
    (1, -1),  
    (-1, 1)   
]



def part1(grid): 
    total = 0 
    for i in range(len(inp)):
        for j in range(len(inp[i])): 
            if inp[i][j] == "X":
                for dx,dy in directions: 
                    x,y = i, j
                    word = ""
                    for k in range(4): 
                        if not (0 <= x < len(inp) and 0 <= y < len(inp[i])):
                            break
                        word += inp[x][y]
                        x += dx
                        y += dy
                    if word == "XMAS": 
                        total += 1
    print(total)

def part2(grid): 
    total = 0
    grid = [list(x) for x in grid]
    rows, cols = len(grid), len(grid[0]) 
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "A":
                if i == 0 or j == 0 or i == len(inp) -1 or j == len(inp[i]) - 1: 
                    continue
                else:  
                    count = 0
                    if i > 0 and j > 0 and i < len(inp) - 1 and j < len(inp[i]) - 1:
                        word1 = inp[i - 1][j- 1] + inp[i][j] + inp[i + 1][j + 1]
                        word2 = inp[i + 1][j - 1] + inp[i][j] + inp[i - 1][j + 1] 
                        word3 = inp[i - 1][j + 1] + inp[i][j] + inp[i + 1][j - 1] 
                        word4 = inp[i + 1][j + 1] + inp[i][j] + inp[i - 1][j - 1]
                        for word in [word1,word2, word3, word4]:
                            if word == "MAS": 
                                count += 1
                    if count  >= 2: 
                        total += 1 
    print(total) 
part2(inp)