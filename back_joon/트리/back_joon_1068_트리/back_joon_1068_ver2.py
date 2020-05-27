import sys
input = sys.stdin.readline

class Node:
    #  노드 클래스에는 노드의 이름(data)와 자식으로 구성되어 있다.
    #  자식이 없으면 None이며 있다면 배열에 저장되도록 구현하였다.
    def __init__(self, data):
        self.data = data
        self.child = None

    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None

    #  자식 노드를 생성하고 추가하는 메소드이다.
    def makeRoot(self, node, child_node):
        if node.child == None :
            node.child = [child_node]
        else :
            node.child.append(child_node)
    
    #  트리에 leaf 과 몇개가 되는지 체크하는 메소드이다.
    def checkLeaf(self, node) :
        leaf = 0
        if node.child == None :
            return 1
        else :
            for l in node.child :
                leaf += self.checkLeaf(l)
        return leaf

    # 트리에서 노드를 제외시키는 메소드이다.     
    def removeNode(self, node) :
        node_dict[upper[remove_node]].child.remove(node_dict[remove_node])
        if len(node_dict[upper[remove_node]].child) == 0 :
            node_dict[upper[remove_node]].child = None



if __name__ == "__main__":
    N = int(input())
    upper = list(map(int, input().split(" ")))
    remove_node = int(input())
    answer = 0
    m_Tree = Tree()
    node_dict = dict()

    #  트리의 노드를 딕셔너리에 정의
    for i in range(N) :
        node_dict[i] = Node(i)
    
    # 루트 노드를 찾고 정의하는 과정
    r_index = upper.index(-1)
    m_Tree.root = node_dict[r_index]

    for i in range(N) :
        if upper[i] != -1 :
            m_Tree.makeRoot(node_dict[upper[i]], node_dict[i])

    #  만약 N 이 1개이거나 삭제헤야 할 노드가 root 노드라면 0을 출력
    if N == 1 or m_Tree.root.data == remove_node:
        print(0)
    else :
        m_Tree.removeNode(node_dict[remove_node])
        answer += m_Tree.checkLeaf(m_Tree.root)
        print(answer)

