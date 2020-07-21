import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.child = None

    def __str__(self):
        return str(self.data)

ansList = []
treeDict = dict()

def checkNodeWeight(k, total) :
    if treeDict[k].child :
        for i in treeDict[k].child :
            checkNodeWeight(i[0], total + i[1])
    else :
        ansList.append(total)


if __name__ == "__main__":
    n = int(input())
    
    while len(treeDict) != n :
        p, c, v = map(int, input().split(' ') )
        if p in treeDict :
            treeDict[p].child.append([c, v])
        else :
            treeDict[p] = Node(p)
            treeDict[p].child = [[c, v]]
        if c not in treeDict :
            treeDict[c] = Node(c)
            treeDict[c].child = []
    checkNodeWeight(1, 0)


    answer = sorted(ansList, key= lambda x: -x)
    print(answer)
        
    print(answer[0] + answer[1])