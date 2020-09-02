import sys
input = sys.stdin.readline

class Node() :
    def __init__(self, data, front) :
        self.data = data
        self.front = front
        self.rear = None


if __name__ == "__main__":
    N, M = map(int, input().split(" ")) 
    nodeDict = dict()
    nodeDict[1] = Node(1, None)
    root = nodeDict[1]
    for i in range(2,N+1) :
        nodeDict[i] = Node(i,nodeDict[i-1])
        nodeDict[i-1].rear = nodeDict[i]
    
    for _ in range(M) :
        a,b = map(int, input().split(" "))
        nodeDict[a].front.rear = nodeDict[a].rear
        if nodeDict[a].rear != None :
            nodeDict[a].rear.front = nodeDict[a].front

        nodeDict[a].rear = nodeDict[b]
        nodeDict[a].front = nodeDict[b].front

        if nodeDict[b].front != None :
            nodeDict[b].front.rear = nodeDict[a]
        nodeDict[b].front = nodeDict[a]

        if nodeDict[a].front == None :
            root = nodeDict[a]
    

    answer = []
    while root.rear != None :
        answer.append(str(root.data))
        root = root.rear
    answer.append(str(root.data))
    result = " ".join(answer)
    print(result)
    

