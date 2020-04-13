# PTA test 完全搜索二叉树


def midorder(bt):  # 利用中序遍历让程序自己找完全二叉树根节点位置
    global cnt, numberlist, cbst
    if bt <= n:
        midorder(bt * 2)
        cbst[bt] = numberlist[cnt]
        cnt += 1
        midorder(bt * 2 + 1)


n = eval(input())
numberlist = [int(i) for i in input().split()]
numberlist.sort()
cnt = 0
cbst = [-1 for i in range(n+1)] # 先把层序的空间开好 下标从1开始 0无意义
midorder(1)
print(" ".join([str(i) for i in cbst[1:]]))
