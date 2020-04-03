# PTA test 并查集


def findroot(pc):  # 找根节点
    global con
    cn = -1
    while con[pc][1] > 0:
        pc = con[pc][1]
        cn -= 1
    if cn > con[pc][1]:
        cn = con[pc][1]
    return pc, cn


def check(c):  # 让我看看有几个子网
    global N
    cnt = 0
    for i in range(1, N + 1):
        if c[i][1] < 0:
            cnt += 1
    c[0][1] = cnt


N = eval(input())
con = [[i, -1] for i in range(N + 1)]
con[0][1] = N  # 第0位代表子网数 后续各位表示是否为根节点
s = input()
while s != 'S':
    status, pc1, pc2 = s.split()
    pc1, pc2 = int(pc1), int(pc2)
    pc1t = findroot(pc1)
    pc1r, con[pc1r][1] = pc1t[0], pc1t[1]
    pc2t = findroot(pc2)
    pc2r, con[pc2r][1] = pc2t[0], pc2t[1]
    if status == 'C':
        if pc1r == pc2r:
            print('yes')
        else:
            print('no')
    elif status == 'I':
        if pc1r != pc2r:
            if con[pc1r][1] < con[pc2r][1]:
                con[pc1r][1] += con[pc2r][1]
                con[pc2r][1] = pc1r
            else:
                con[pc2r][1] += con[pc1r][1]
                con[pc1r][1] = pc2r
    s = input()
check(con)
if con[0][1] == 1:
    print('The network is connected.')
else:
    print('There are %d components.' % con[0][1])
