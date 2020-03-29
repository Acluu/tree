# PTA test AVL tree
class Node:
    def __init__(self, data=-1, left=None, right=None, height=0):
        self.data = data
        self.left = left
        self.right = right
        self.height = height


class Tree:
    def __init__(self, root=None):
        self.root = root


def leftrot(tree):
    ltpt = tree.left
    tree.left = ltpt.right
    ltpt.right = tree
    tree.height = max(height(tree.left), height(tree.right)) + 1
    ltpt.height = max(height(ltpt.left), tree.height) + 1
    return ltpt


def rightrot(tree):
    ltpt = tree.right
    tree.right = ltpt.left
    ltpt.left = tree
    tree.height = max(height(tree.left), height(tree.right)) + 1
    ltpt.height = max(height(ltpt.right), tree.height) + 1
    return ltpt

def lrrot(A):
    A.left = rightrot(A.left)
    return leftrot(A)


def rlrot(A):
    A.right = leftrot(A.right)
    return rightrot(A)

def insert(tree, data):
    if tree is None:
        tree = Node(data)
        tree.height = 1
    elif data < tree.data:
        tree.left = insert(tree.left, data)
        if height(tree.left) - height(tree.right) == 2:
            if data < tree.left.data:
                tree = leftrot(tree)
            else:
                tree = lrrot(tree)
    elif data > tree.data:
        tree.right = insert(tree.right, data)
        if height(tree.right) - height(tree.left) == 2:
            if data > tree.right.data:
                tree = rightrot(tree)
            else:
                tree = rlrot(tree)

    tree.height = max(height(tree.left), height(tree.right)) + 1
    #循环实现爬
    '''newnode = Node(data)
    while 1:
        if tnode.data < data:
            if tnode.right is not None:
                tnode = tnode.right
            else:
                tnode.right = newnode
                break
        elif tnode.data > data:
            if tnode.left is not None:
                tnode = tnode.left
            else:
                tnode.left = newnode
                break'''
    return tree


def height(tree):
    if tree is not None:
        hl = height(tree.left)
        hr = height(tree.right)
        h = hl if hl > hr else hr
        return h+1
    return 0


num = eval(input())
nodelist = [int(i) for i in input().split()]
rnode = Node(nodelist[0])
for data in nodelist[1:]:
    rnode = insert(rnode, data)
print(rnode.data)
