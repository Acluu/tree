# PTA test saving 007


def firstjump(c):
    tx, ty = c
    if (tx ** 2 + ty ** 2) <= ((15 + D) ** 2):
        return 1
    return 0


def jump(v1, v2):
    if ((v1[0]-v2[0]) ** 2 + (v1[1]-v2[1]) ** 2) <= (D ** 2):
        return 1
    return 0


def dfs(c):
    global answer
    cod[c][1] = 1
    if cod[c][0] == 1:
        answer = 1
    for cc in cod:
        if (cod[cc][1] == 0) & (jump(c, cc)):
            answer = dfs(cc)
            if answer == 1:
                break
    return answer


answer = 0
N, D = map(int, input().split())
cod = {}  # 包含(x,y):(safe,visited) 前两位坐标 safe为能否跳出 visited为是否访问
for i in range(N):
    x, y = map(int, input().split())
    Max, Min = max(x, y), min(x, y)
    safe = 1 if (Max >= 50 - D) | (Min <= -50 + D) else 0
    cod[(x, y)] = [safe, 0]
for cro in cod:
    if (cod[cro][1] == 0) & (firstjump(cro)):
        answer = dfs(cro)
        if answer == 1:
            break
    else:
        answer = 0
if answer == 1:
    print('Yes')
else:
    print('No')
