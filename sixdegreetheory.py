# PTA test 六度空间


class Queue:
    def __init__(self):
        self.li = []

    def delete(self):
        return self.li.pop(0)

    def add(self, item):
        self.li.append(item)


def bfs1(node):
    global adlist, visited1, N, level1
    tq = Queue()
    visited1[node] = 1
    tq.add(node)
    level1[node] = 0
    while tq.li:
        tn = tq.delete()
        for item in adlist[tn]:
            if visited1[item] == 0:
                visited1[item] = 1
                tq.add(item)
                level1[item] = level1[tn] + 1
        if max(level1) == 7:
            return


'''
def bfs(node):
    global graph, visited, N, level
    tq = Queue()
    visited[node] = 1
    tq.add(node)
    level[node] = 0
    while tq.li:
        tn = tq.delete()
        for i in range(N):
            if (graph[tn][i] == 1) & (visited[i] == 0):
                visited[i] = 1
                tq.add(i)
                level[i] = level[tn] + 1
        if 7 in level:
            return'''

N, M = map(int, input().split())
# graph = [[0 for i in range(N)] for j in range(N)]
adlist = [[] for i in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    x, y = max(x, y), min(x, y)
    adlist[x - 1].append(y - 1)
    adlist[y - 1].append(x - 1)
    # graph[x-1][y-1] = graph[y-1][x-1] = 1
# level = [114514 for i in range(N)]
level1 = [-1 for i in range(N)]
# visited = [0 for i in range(N)]
visited1 = [0 for i in range(N)]
for i in range(N):
    # bfs(i)
    bfs1(i)
    # total = len([k for k in level if k <= 6])
    total1 = len([k for k in level1 if (k <= 6) & (k >= 0)])
    # print("%d: %.2f%%" % (i+1, total/N*100))
    print("%d: %.2f%%" % (i + 1, total1 / N * 100))
    # level = [114514 for i in range(N)]
    # visited = [0 for i in range(N)]
    level1 = [-1 for i in range(N)]
    visited1 = [0 for i in range(N)]
