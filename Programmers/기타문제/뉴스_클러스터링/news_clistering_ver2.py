import math
def makeSet (strings) :
    sets_dict = dict()
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
            if temp in sets_dict :
                sets_dict[temp] += 1
            else :
                sets_dict[temp] = 1 
            
    return sets_dict

def solution(str1, str2):
    A = makeSet(str1)
    B = makeSet(str2)
    interSet = 0
    unionSet = 0
    #  합집합에서 사용할 키!
    union_keys = (set(list(A.keys()) + list(B.keys())))

    # 교집합의 수 구하기
    for i_key in A.keys() :
        if i_key in B :
            interSet += min(A[i_key], B[i_key])
    
    # 합집합의 수 구하기
    for i_key in union_keys :
        if i_key in A and i_key in B:
            unionSet += max(A[i_key], B[i_key])
        elif i_key in A :
            unionSet += A[i_key]
        elif i_key in B :
            unionSet += B[i_key]

    
    jacard = 0
    if interSet == 0 and unionSet == 0 :
        jacard = 65536
    else :
        jacard = math.floor(interSet/unionSet * 65536)

    return jacard

print(solution("FRANCE", "french"))