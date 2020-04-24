# PTA test
# UTF-8


MAX = float("inf")

def readgraph(N, M):
    g = [[MAX for j in range(N)] for i in range(N)]
    for i in range(M):
        x, y, w = map(int, input().split())
        g[x-1][y-1] = g[y-1][x-1] = w
    return g


def floyd(g, N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if g[i][k] + g[k][j] < g[i][j]:
                    g[i][j] = g[i][k] + g[k][j]


def secmax(l, i):
    return sorted(l, reverse=True)[1]


N, M = [int(i) for i in input().split()]
graph = readgraph(N, M)
floyd(graph, N)
animal = 0
tm = MAX
for i in range(len(graph)):
    t = secmax(graph[i], i)
    if t == MAX:
        print(0)
        exit(0)
    if t < tm:
        tm = t
        animal = i+1
print(animal, tm)
