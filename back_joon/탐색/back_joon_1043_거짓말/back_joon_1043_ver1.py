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
    bfs = [True for i in range(N+1)]
    for i in real[1:] :
        rDict[i] = True
        bfs[i] = False
    party = []
    for _ in range(M) :
        temp = list(map(int, input().split(" ")))
        party.append(temp)
        for i in temp :
            if i in rDict :
                for j in temp :
                    bfs[j] = False
                break
    for i in party :
        for j in i :
            if not bfs[j] :
                answer -= 1
                break
    return answer

if __name__ == "__main__":
    print(soluction())
    

    