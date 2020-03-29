# UTF-8
# PTA test


def isomorphic(r1, r2):
    global tree1, tree2
    if (r1 is -1) & (r2 is -1):
        return 1
    if ((r1 is -1) & (r2 is not -1)) | ((r1 is not -1) & (r2 is -1)):
        return 0
    if tree1[r1][0] != tree2[r2][0]:
        return 0
    if (tree1[r1][1] is -1) & (tree2[r2][1] is -1):
        return isomorphic(tree1[r1][2], tree2[r2][2])
    if (tree1[r1][1] is not -1) & (tree2[r2][1] is not -1) & (tree1[tree1[r1][1]][0] == tree2[tree2[r2][1]][0]):
        return (isomorphic(tree1[r1][1], tree2[r2][1])) & (isomorphic(tree1[r1][2], tree2[r2][2]))
    else:
        return (isomorphic(tree1[r1][1], tree2[r2][2])) & (isomorphic(tree1[r1][2], tree2[r2][1]))
    return 0


n1 = eval(input())
tree1, tree2 = [], []
if n1 != 0:
    check1 = [0 * i for i in range(n1)]
    for i in range(n1):
        ele, l, r = input().split()
        if l != '-':
            l = int(l)
            check1[l] = 1
        else:
            l = -1
        if r != '-':
            r = int(r)
            check1[r] = 1
        else:
            r = -1
        tree1.append([ele, l, r])
n2 = eval(input())
if n2 != 0:
    check2 = [0 * i for i in range(n2)]
    for i in range(n2):
        ele, l, r = input().split()
        if l != '-':
            l = int(l)
            check2[l] = 1
        else:
            l = -1
        if r != '-':
            r = int(r)
            check2[r] = 1
        else:
            r = -1
        tree2.append([ele, l, r])
if (n1 == 0)&(n2 == 0):
    print('Yes')
    exit(0)
root1 = check1.index(0) if 0 in check1 else -1
root2 = check2.index(0) if 0 in check2 else -1

if isomorphic(root1, root2):
    print('Yes')
else:
    print('No')
