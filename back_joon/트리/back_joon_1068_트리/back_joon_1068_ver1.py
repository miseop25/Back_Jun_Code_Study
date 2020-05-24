import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.child = None

    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None

    def makeRoot(self, node, child_node):
        if self.root == None:
            self.root = node
        if node.child == None :
            node.child = [child_node]
        else :
            node.child.append(child_node)
    
    def checkLeaf(self, node) :
        leaf = 0
        if node.child == None :
            return 1
        else :
            for l in node.child :
                leaf += self.checkLeaf(l)
        return leaf
    
    def removeNode(self, node) :
        node.child = None
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
    for i in range(N) :
        node_dict[i] = Node(i)
    
    for i in range(N) :
        if upper[i] != -1 :
            m_Tree.makeRoot(node_dict[upper[i]], node_dict[i])

    if N == 1 :
        print(0)
    elif m_Tree.root.data == remove_node :
        if len(m_Tree.root.child) == 1 :
            m_Tree.root = m_Tree.root.child[0]
            answer += m_Tree.checkLeaf(m_Tree.root)
            print(answer)
        else :
            print(0)
    else :
        m_Tree.removeNode(node_dict[remove_node])
        answer += m_Tree.checkLeaf(m_Tree.root)
        print(answer)



