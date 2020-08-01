import sys
sys.setrecursionlimit(10000000)
def solution(n, edge):
    answer = 1
    nodeDict = dict()
    bfs = [-1] * (n+1)
    for i in range(1, n+1) :
        nodeDict[i] = []
    for a, b in edge :
        nodeDict[a].append(b)
        nodeDict[b].append(a)
    bfs[0] = 0
    bfs[1] = 0

    def checkLen(node) :
        for i in nodeDict[node] :
            if bfs[i] == -1 :
                bfs[i] = bfs[node] + 1
                checkLen(i)
            # else :
            #     if bfs[i] > bfs[node] + 1 and bfs[i] != -1 :
            #         bfs[i] = bfs[node] + 1
            #         checkLen(i)
                
    checkLen(1)
    result = list(sorted(bfs, key= lambda x: -x))
    comp = result[0]
    for i in result[1:] :
        if i == comp :
            answer += 1
        else : 
            break
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
print(solution(2, [[1,2]]) )