# 再战PTA线性结构


class Node:
    def __init__(self, address=None, data=-1, pre=None, nex=None, naddress=None):
        self.data = data
        self.address = address
        self.pre = pre
        self.nex = nex
        self.naddress = naddress


from collections import OrderedDict

# PTA Reversing Linked List

curad, N, k = input().split()
N, k = int(N), int(k)
tpt = [k for k in input().split()]
rnode = Node(-1, -1)
tnode = Node(tpt[0], tpt[1], rnode, naddress=tpt[2])
rnode.nex = tnode

for i in range(N-1):
    tpt = [k for k in input().split()]
    tptnode = Node(tpt[0], tpt[1], tnode, naddress=tpt[2])
    tnode.nex = tptnode
    tnode = tptnode

enode = Node
tnode.nex = enode
enode.pre = tnode
cc = enode.pre
while cc.pre is not None:
    print(cc.data, cc.address)
    cc=cc.pre
