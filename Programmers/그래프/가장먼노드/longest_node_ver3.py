from collections import deque, defaultdict

def solution(n, edge):
    answer = 1
    nodeDict = defaultdict(list)
    bfs = {i:0 for i in range(1, n+1)}
    

    for a, b in edge :
        nodeDict[a].append(b)
        nodeDict[b].append(a)
    
    q = deque(nodeDict[1])
    dis = 1
    while q :
        for i in range(len(q)) :
            v = q.popleft()
            if bfs[v] == 0 :
                bfs[v] = dis
                for w in nodeDict[v] :
                    q.append(w)
        dis += 1
    del bfs[1]

    result = list(sorted(bfs.values(), key= lambda x: -x))
    comp = result[0]
    for i in result[1:] :
        if i == comp :
            answer += 1
        else : 
            break
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
print(solution(2, [[1,2]]) )