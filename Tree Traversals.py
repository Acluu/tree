# 数据结构mooc课后题
# 处理输入 存为前序和中序


def dbf(pre, mid):
    global poslist
    if len(pre) == 1:
        poslist.insert(0, pre[0])
        return
    troot = pre[0]
    poslist.insert(0, troot)
    rootloc = mid.index(troot)
    mleft = mid[:rootloc]
    mright = mid[rootloc+1:]
    pleft = pre[1:rootloc+1]
    pright = pre[rootloc+1:]
    if len(mright) != 0:
        dbf(pright,mright)
    if len(mleft) != 0:
        dbf(pleft,mleft)


poslist = []
elenum = eval(input())
prelist = []
tstack = []
midlist = []
for i in range(2*elenum):
    temp = input()
    if temp[1] == 'u':
        prelist.append(eval(temp.split()[1]))
        tstack.append(eval(temp.split()[1]))
    else:
        midlist.append(tstack.pop())
dbf(prelist, midlist)
print(" ".join([str(i) for i in poslist]))
