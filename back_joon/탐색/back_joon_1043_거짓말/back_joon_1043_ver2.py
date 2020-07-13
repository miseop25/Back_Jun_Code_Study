import sys
input = sys.stdin.readline

def soluction() :
    N, M = map(int, input().split(" "))
    real = list(map(int, input().split(" ")))
    answer = M
    knowTrue = real[0]
    if knowTrue == N : return 0
    if knowTrue == 0 : return M
    rDict = dict()
    person = dict()
    for i in range(1, N+1) :
        person[i] = set()

    for i in real[1:] :
        rDict[i] = [True, set()]
        
    party = []
    for p in range(M) :
        temp = list(map(int, input().split(" ")))
        for i in temp :
            person[i].add(p)
            if i in rDict :
                rDict[i][1].add(p)

        party.append([True, temp])

    flag = True 
    while flag :
        flag = False
        for k, v in rDict.items() :
            if v[0] :
                rDict[k][0] = False 
                for i in v[1] :
                    party[i][0] = False
                    for p in party[i][1] :
                        if p not in rDict :
                            rDict[p] = [True, person[p]]
            
    print(rDict)
    print(person)
    print(party)
    return answer

if __name__ == "__main__":
    print(soluction())
    

    