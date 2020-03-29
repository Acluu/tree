# PTA判断是否为同一二叉搜索树


class Node:
    def __init__(self, data=-1, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root=None):
        self.root = root


def insert(tree, data):
    tnode = tree.root
    newnode = Node(data)
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
                break
    return tree


def preorder(tpt, prelist):
    if tpt is not None:
        prelist.append(tpt.data)
    if tpt.left is not None:
        preorder(tpt.left, prelist)
    if tpt.right is not None:
        preorder(tpt.right, prelist)


initial = input()
if len(initial) == 1:
    exit(0)
elenum, listnum = [int(i) for i in initial.split()]
while len(initial) != 1:
    elenum, listnum = [int(i) for i in initial.split()]
    comlist = [int(i) for i in input().split()]
    rootnode = Node(comlist[0])
    comtree = Tree(rootnode)
    comtreepre = []
    for i in range(len(comlist)-1):
        comtree = insert(comtree, comlist[i+1])
    preorder(comtree.root, comtreepre)
    for _ in range(listnum):
        calist = [int(i) for i in input().split()]
        rnode = Node(calist[0])
        catree = Tree(rnode)
        catreepre = []
        for i in range(len(calist) - 1):
            catree = insert(catree, calist[i + 1])
        preorder(catree.root, catreepre)
        if catreepre == comtreepre:
            print('Yes')
        else:
            print('No')
    initial = input()
