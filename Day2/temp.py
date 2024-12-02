#8 6 4 4 1
arr = [-2,-2,0,-3]
print(all(d < 0 for d in arr))


def check(line):
    diffs = []
    for char in range(len(line)-1):
        diffs.append(int(line[char+1]) - int(line[char]))
    # Should check if all numbers are going up/down and have a 1 to 3 difference
    if (all(d > 0 for d in diffs) or all(d < 0 for d in diffs)):
        if all(abs(d) in range(1, 4) for d in diffs):
            return True
    return False