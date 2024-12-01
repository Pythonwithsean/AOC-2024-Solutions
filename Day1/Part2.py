import collections

string = """
"""

def parse(sting): 
    if string != "":
        return string

def solution(s): 
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

solution(string)