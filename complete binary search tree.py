# PTA test 完全搜索二叉树

def midorder(bt):
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
cbst = [i*0-1 for i in range(n+1)]
midorder(1)
print(" ".join([str(i) for i in cbst[1:]]))


