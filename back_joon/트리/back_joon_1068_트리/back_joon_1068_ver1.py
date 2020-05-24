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


if __name__ == "__main__":
    N = int(input())
    upper = list(map(int, input().split(" ")))
    remove_node = int(input())
    m_Tree = Tree()
    node_dict = dict()
    for i in range(N) :
        node_dict[i] = Node(i)
    
    for i in range(N) :
        if upper[i] != -1 :
            m_Tree.makeRoot(node_dict[upper[i]], node_dict[i])
    print(m_Tree.root)
    print(node_dict)    


