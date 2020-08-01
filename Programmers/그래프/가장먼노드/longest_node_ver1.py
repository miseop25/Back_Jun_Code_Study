import copy
def solution(n, edge):
    answer = 0
    distence = dict()
    nodeDict = dict()
    bfs = [True] * (n+1)
    for i in range(1, n+1) :
        nodeDict[i] = []
        distence[i] = None
    for a, b in edge :
        nodeDict[a].append(b)
        nodeDict[b].append(a)

    def checkLen(node, dis, myBfs) :
        dis += 1
        if distence[node] == None :
            distence[node] = dis
        else :
            if distence[node] > dis :
                distence[node] = dis

        myBfs[node] = False
        for i in nodeDict[node] :
            if myBfs[i] :
                checkLen(i, dis, copy.deepcopy(myBfs))

    dis = 0
    bfs[1] = False
    distence[1] = 0
    for i in nodeDict[1] :
        myBfs = copy.deepcopy(bfs)
        checkLen(i, dis, myBfs)
    print(distence)
    result = list(sorted(distence.items(), key= lambda x: -x[1]))
    comp = result[0][1]
    for i in result :
        if comp == i[1] :
            answer += 1
        else : 
            return answer
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))