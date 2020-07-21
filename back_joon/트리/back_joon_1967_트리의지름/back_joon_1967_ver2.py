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

    if len(treeDict[k].child) >= 2 :
        result = []
        for i in treeDict[k].child :
            s = i[1]
            s += checkNodeWeight(i[0], total + i[1]) - total
            result.append(s)
        result = sorted(result, reverse= True)
        ansList.append(result[0] + result[1])
        return result[0]
    elif len(treeDict[k].child) == 1 :
        return checkNodeWeight(treeDict[k].child[0][0], total + treeDict[k].child[0][1])
    else :
        ansList.append(total)
        return total


if __name__ == "__main__":
    n = int(input())
    
    while len(treeDict) != n and n != 1 :
        p, c, v = map(int, input().split(' ') )
        if p in treeDict :
            treeDict[p].child.append([c, v])
        else :
            treeDict[p] = Node(p)
            treeDict[p].child = [[c, v]]
        if c not in treeDict :
            treeDict[c] = Node(c)
            treeDict[c].child = []
    if n > 2 :
        a = checkNodeWeight(1, 0)
        answer = sorted(ansList, key= lambda x: -x)
        print(answer[0])
    elif  n == 2:
        print(v)
    else :
        print(0)
        