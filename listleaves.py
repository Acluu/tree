# utf-8
# pta test 前序遍历打印叶子结点
queue = []
def gogogo(tr, ro):
    print(ro)
    if tr[ro][0] != '-':
        gogogo(tr, tr[ro][0])
   # if tr[ro][0] == tr[ro][1]:

    if tr[ro][1] != '-':
        gogogo(tr, tr[ro][1])
    return 0


out = ''

def cengxu(tr, ro):
    global queue, n, out
    queue.append(tr[ro])
    while(queue != []):
        cur = queue[0]
        del queue[0]
        if cur[0] == cur[1]:
            out = out+str(cur[-1])+' '
        if cur[0] != '-':
            queue.append(tr[cur[0]])
        if cur[1] != '-':
            queue.append(tr[cur[1]])


n = eval(input())
tree = []
check = [0 * n for i in range(n)]
for i in range(n):
    l, r = input().split()
    if l != '-':
        l = int(l)
        check[l] = 1
    if r != '-':
        r = int(r)
        check[r] = 1
    tree.append([l, r, i])
root = check.index(0)
cengxu(tree, root)
print(out.strip())