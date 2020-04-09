# PTA test 联通集


class Queue:
    def __init__(self):
        self.li = []

    def delete(self):
        return self.li.pop(0)

    def add(self, item):
        self.li.append(item)


def out(setlist):
    if not setlist:
        return
    s = '{ '
    for il in setlist:
        s = s + str(il) + ' '
    s += '}'
    print(s)


def bfs(node):
    global graph, visited, nv, tist
    tq = Queue()
    visited[node] = 1
    tist.append(node)
    tq.add(node)
    while tq.li:
        tn = tq.delete()
        for i in range(nv):
            if (graph[tn][i] == 1) & (visited[i] == 0):
                visited[i] = 1
                tist.append(i)
                tq.add(i)


def dfs(node):
    global graph, visited, nv, tist
    visited[node] = 1
    tist.append(node)
    for im in range(nv):
        if (graph[node][im] == 1) & (visited[im] == 0):
            dfs(im)


nv, ne = map(int, input().split())
graph = [[0 for i in range(nv)] for j in range(nv)]
for i in range(ne):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = graph[v2][v1] = 1
visited = [0 for i in range(nv)]
tist = []
for i in range(nv):
    if visited[i] == 0:
        dfs(i)
    out(tist)
    tist = []
visited = [0 for i in range(nv)]
for i in range(nv):
    if visited[i] == 0:
        bfs(i)
    out(tist)
    tist=[]

