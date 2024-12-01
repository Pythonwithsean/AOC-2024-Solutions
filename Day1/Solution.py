import collections
string = """
76569   66648
38663   66530
60350   60777
35330   13469
88681   66648
30057   83262
55455   13469
48398   40350
"""


def part1(s): 
    rows = [x for x in s.strip().split("\n")]
    list1 = list()
    list2 = list()
    for i in range(len(rows)): 
        rows[i] = rows[i].strip().split("   ")
        list1.append(int(rows[i][0]))
        list2.append(int(rows[i][1]))
    list1.sort()
    list2.sort()
    total = 0
    for x,y in [x for x in zip(list1, list2)]: 
        total += abs(x -y)
    print(total) 

def part2(s): 
    rows = [x for x in s.strip().split("\n")]
    list1 = []
    list2 = []
    total = 0
    for i in range(len(rows)): 
        rows[i] = rows[i].strip().split("   ")
        list1.append(int(rows[i][0]))
        list2.append(int(rows[i][1]))
    count = collections.Counter(list2)
    for x in list1:
        total += x *count.get(x,0)
    print(total)