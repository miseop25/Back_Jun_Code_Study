import math
def makeSet (strings) :
    sets = []
    for i in range(len(strings) -1) :
        temp = strings[i : i +2]
        temp = temp.lower()
        check = True
        for t in temp : 
            if t >= "a" and t <= "z" :
                pass 
            else :
                check = False
                break
        if check :
            sets.append(temp)    
    return sets

def solution(str1, str2):
    A = makeSet(str1)
    B = makeSet(str2)
    interSet = len(A.intersection(B) )
    unioSet = len(A.union(B))
    jacard = 0
    if interSet == 0 and unioSet == 0 :
        jacard = 65536
    else :
        jacard = math.floor(interSet/unioSet * 65536)

    return jacard

print(solution("aa1+aa2", "AAAA12"))