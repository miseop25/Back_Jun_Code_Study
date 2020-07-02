import itertools
def solution(nums):
    answer = 0
    result = list(itertools.combinations(nums, 3))
    prims = [True for i in range(3001)]
    prims[0] = False
    prims[1] = False
    for i in range(2 , 3001) :
        if prims[i] :
            for j in range(2*i, 3001, i) :
                prims[j] = False
    
    for i in result :
        temp = sum(i)
        if prims[temp] :
            answer += 1

    return answer