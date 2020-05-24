import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None

    def preorderTraversal(self, node):
        print(node, end='')
        if not node.left  == None : self.preorderTraversal(node.left)
        if not node.right == None : self.preorderTraversal(node.right)

    def inorderTraversal(self, node):
        if not node.left  == None : self.inorderTraversal(node.left)
        print(node, end='')
        if not node.right == None : self.inorderTraversal(node.right)

    def postorderTraversal(self, node):
        if not node.left  == None : self.postorderTraversal(node.left)
        if not node.right == None : self.postorderTraversal(node.right)
        print(node, end='')

    def makeRoot(self, node, left_node, right_node):
        if self.root == None:
            self.root = node
        node.left = left_node
        node.right = right_node


if __name__ == "__main__" :
    N  = int(input())
    m_Tree = Tree()
    buf = []
    nodes_dict = dict()
    step = []
    for _ in range(N) :
        temp = list(map(str, input().split(" ")))
        temp[2] = temp[2][:-1]
        for i in range(3) :
            if temp[i] not in buf and temp[i] != "." :
                buf.append(temp[i])
                nodes_dict[temp[i]] = Node(temp[i])
            if temp[i] == "." :
                temp[i] = None
        step.append(temp)

    for i in step :
        if i[1] == None and i[2] == None:
            m_Tree.makeRoot(nodes_dict[i[0]],None,None)
        elif i[1] == None :
            m_Tree.makeRoot(nodes_dict[i[0]],None,nodes_dict[i[2]])
        elif i[2] == None :
            m_Tree.makeRoot(nodes_dict[i[0]],nodes_dict[i[1]],None)
        else :
            m_Tree.makeRoot(nodes_dict[i[0]],nodes_dict[i[1]],nodes_dict[i[2]])


    print(end=''); m_Tree.preorderTraversal(m_Tree.root)
    print('\n', end=''); m_Tree.inorderTraversal(m_Tree.root)
    print('\n', end=''); m_Tree.postorderTraversal(m_Tree.root)
    

