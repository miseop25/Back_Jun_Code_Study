from collections import deque
class Node :
    def __init__(self,index, x) :
        self.data = index + 1
        self.x = x
        self.left = None
        self.right = None

class Tree :
    def __init__(self, root,nodeDict) :
        self.root = root
        self.nDict = nodeDict


def solution(nodeinfo):
    answer = [[]]
    nodeDict = dict()
    rootKey = 0
    for i in range(len(nodeinfo)) :
        x = nodeinfo[i][0]
        y = nodeinfo[i][1]
        if rootKey < y :
            rootKey = y
        if y in nodeDict :
            nodeDict[y].append([x, Node(i, x)])
        else :
            nodeDict[y] = deque([[x, Node(i, x)]])
    
    t = sorted(nodeDict.items(), key= lambda x: -x[0])

    alpa = deque(sorted(test[1], key= lambda x: x[0]))
    while alpa :
        a = alpa.popleft()
        print(a)
    
    return answer



print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))