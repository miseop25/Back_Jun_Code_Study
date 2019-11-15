from itertools import combinations

def solution(clothes):
    answer = 0
    wear = dict()
    for i in clothes :
        #if i[1] in wear.keys() :
        if wear.get(i[1],None) :        #이렇게 하는 것이 더 효율적이다!
            wear[i[1]] +=1
        else :
            wear[i[1]] = 1

            
    wear_list = list(wear.values())
    if len(wear_list) == 30 :
        return len(clothes)
    if len(wear) != 1 :
        for i in range(1 ,len(wear_list)+1) :
            buf = list( combinations(wear_list, i))
            for k in buf :
                sum = 1
                for j in k : 
                    sum = sum*j
                answer += sum
    else :
        answer =  len(clothes)
    
    return answer


cl = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
print(solution(cl))