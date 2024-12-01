string = """
"""

def parse(sting): 
    if string != "":
        return string


def solution(s): 
    rows = [x for x in s.strip().split("\n")]
    list1 = []
    list2 = []
    for i in range(len(rows)): 
        rows[i] = rows[i].strip().split("   ")
        list1.append(int(rows[i][0]))
        list2.append(int(rows[i][1]))
    list1.sort()
    list2.sort()
    arr = [x for x in zip(list1, list2)]
    total = 0
    for x,y in arr: 
        total += abs(x -y)
    print(total)
        

    
        
    

solution(string)