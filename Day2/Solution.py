from Helper import parseFile

def part1():
    inp = parseFile("./input.txt")[1]
    total = 0
    for i in range(len(inp)):
        line = inp[i]
        inp[i] = [x for x in map(int, line)]
    for i in range(len(inp)): 
        if validSteps(inp[i])[0]:
            total += 1
    print(total)
    
def parse(line): 
    temp  = []  
    for i in range(len(line) - 1): 
        temp.append(line[i] -  line[i + 1])
    temp.append(line[i] - line[i+ 1])
    return temp

def validSteps(line):
        # Increasing
        if line[0] < line[1]:
            valid, index = increase(line)
            return valid, index
        # Decrease
        else:
            valid, index = decrease(line)
            return valid, index

    
def increase(line): 
    for i in range(1,len(line)): 
        if line[i - 1] > line[i] or abs(line[i] - line[i - 1]) not in range(1,4): 
            return False, i
    return True, -1


def decrease(line): 
    for i in range(1,len(line)): 
        if line[i - 1] < line[i] or abs(line[i] - line[i - 1]) not in range(1,4): 
            return False, i
    return True, -1

            
         

def part2():
    inp = parseFile("./input.txt")[1]
    for i in range(len(inp)):
        line = inp[i]
        inp[i] = [x for x in map(int, line)]
    total = 0
    for i in range(len(inp)): 
        valid, index = validSteps(inp[i])
        if valid and index == -1:
            total += 1
        else:
            for j in range(len(inp[i])): 
                rest = inp[i][:j] + inp[i][j+1:]
                valid, index = validSteps(rest)
                print(valid,index,rest)
                if valid and index == -1:
                    total += 1
                    break 
    print(total)


if __name__ == "__main__":
    # part1()
    part2()