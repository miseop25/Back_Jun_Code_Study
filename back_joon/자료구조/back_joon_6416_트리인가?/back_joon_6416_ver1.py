import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.child = None
        self.parant = None

    def __str__(self):
        return str(self.data)

    
def soluction() :

    def checkCycle(rootNode) :
        cnt = len(rootNode.child)
        for i in rootNode.child :
            cnt += checkCycle(node_dict[i])
        return cnt

    isInput = True
    answer = True
    node_dict = dict()
    root = None
    global isWorking

    while isInput :
        buf = input().rstrip().split("  ")
        if buf[0] == '' :
            continue
        for temp in buf :
            a, b = map(int , temp.split(" "))
            if a == 0 and b == 0 :
                isInput = False
                break
            elif a < 0 and b < 0:
                isWorking = False
                isInput = False
                break
            # node를 딕셔너리에 저장한다.
            if a in node_dict :
                node_dict[a].child.append(b)
            else :
                node_dict[a] = Node(a)
                node_dict[a].child = [b]
            if b in node_dict :
                # 부모가 2명(들어오는 간선의 수가 2개이면 안된다.)일 순 없다
                if node_dict[b].parant == None :
                    node_dict[b].parant = a
                else :
                    answer = False
            else :
                node_dict[b] = Node(b)
                node_dict[b].parant = a
                node_dict[b].child = []
    #  공배열도 트리이다.
    if len(node_dict) == 0 :
        return True
    if answer == False :
        return answer
    #  루트 노드 찾기 and 부모가 없는 노드가 2개이면 한개의 트리가 아니다.
    for v in node_dict.values() :
        if v.parant == None :
            if root == None :
                root = v.data
            else :
                answer = False
                return answer
    # 루트가 없어도 트리가 이나다.
    if root == None :
        return False

    #  루트로부터 시작해서 모든 노드로 갈 수 있어야 한다.
    cycle = 1 + len(node_dict[root].child)
    for i in node_dict[root].child :
        cycle += checkCycle(node_dict[i])
    if cycle != len(node_dict) :
        return False
    return answer


if __name__ == "__main__":
    isWorking = True
    num = 1
    while isWorking :
        check = soluction()
        if not isWorking :
            break
        if check :
            string = "Case " + str(num) + " is a tree."
            print(string)
        else :
            string = "Case " + str(num) + " is not a tree."
            print(string)
        num += 1

    