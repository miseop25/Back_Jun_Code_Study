def solution(participant, completion):
    c1Dict = dict()
    c2Dict = dict()
    for i in completion :
        if i in c1Dict :
            c1Dict[i] += 1
        else : 
            c1Dict[i] = 1
    
    for i in participant :
        if i not in c1Dict :
            return i
        if i in c2Dict :
            c2Dict[i] += 1
        else :
            c2Dict[i] = 1
    
    for k, v in c1Dict.items() :
        if v != c2Dict[k] :
            return k
        
