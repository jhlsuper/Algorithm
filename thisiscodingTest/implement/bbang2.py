import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 0, 0, 1]  ## 상 좌 우 하
dy = [0, -1, 1, 0]
n, m = map(int, input().split())
arr = [[0 for _ in range(n + 1)]]
base = []

for i in range(1, n + 1):
    temp = [0] + list(map(int, input().strip().split()))
    for j in range(1, n + 1):
        if temp[j] == 1:
            base.append((i, j))
    arr.append(temp)

store = [list(map(int, input().strip().split())) for _ in range(m)]

check = [[0 for _ in range(n + 1)] for _ in range(n + 1)]


def storetobase(x, y, bx, by):
    q = deque()
    visited = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    q.append((x, y))
    visited[x][y] = 1

    while q:
        cx, cy = q.popleft()
        if cx == bx and cy == by:
            return visited[cx][cy] - 1
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 1 <= nx < n + 1 and 1 <= ny < n + 1 and not visited[nx][ny] and not check[nx][ny]:
                visited[nx][ny] = visited[cx][cy] + 1
                q.append((nx, ny))
    return -1


def findbase(sx, sy):
    temp = []

    for bx, by in base:
        if not check[bx][by]:
            dis = storetobase(sx, sy, bx, by)

            if dis != -1:
                temp.append((dis, bx, by))

    if temp:
        temp.sort(key=lambda x: (x[0], x[1], x[2]))
        return temp[0][1], temp[0][2]
    else:
        return -1, -1


def gotostore(x, y, sx, sy, d):
    q = deque()
    visited = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    visited[x][y] = 1
    nx, ny = x + dx[d], y + dy[d]
    fnx, fny = nx, ny
    if 1 <= nx < n + 1 and 1 <= ny < n + 1 and not check[nx][ny]:
        visited[nx][ny] = 2
        q.append((nx, ny))
    else:
        return sys.maxsize, 0, 0
    while q:
        px, py = q.popleft()
        if px == sx and py == sy:
            return visited[px][py] - 1, fnx, fny
        for i in range(4):
            nx, ny = px + dx[i], py + dy[i]

            if 1 <= nx < n + 1 and 1 <= ny < n + 1 and not check[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = visited[px][py] + 1
                q.append((nx, ny))
    return sys.maxsize, 0, 0


poslist = [[] for _ in range(m)]
time = 1

sx, sy = store[0]
bx, by = findbase(sx, sy)
poslist[0] = [bx, by]
check[bx][by] = 1

stop = [0 for _ in range(m)]
count = 0
while count < m:
    time += 1
    tempgo = [(0, 0) for _ in range(m)]
    for i in range(m):
        if poslist[i] and not stop[i]:
            sx, sy = store[i]
            x, y = poslist[i]
            min_dis = sys.maxsize
            minfx, minfy = 0, 0

            for d in range(4):
                dis, fx, fy = gotostore(x, y, sx, sy, d)
                if min_dis > dis:
                    min_dis = dis
                    minfx, minfy = fx, fy
            tempgo[i] = (minfx, minfy)
    for i, (fx, fy) in enumerate(tempgo):
        if store[i][0] == fx and store[i][1] == fy:
            poslist[i] = [fx, fy]
            check[fx][fy] = 1
            stop[i] = 1
            count += 1
        else:
            poslist[i] = [fx, fy]
    if time <= m:
        bx, by = findbase(store[time - 1][0], store[time - 1][1])
        poslist[time - 1] = [bx, by]
        check[bx][by] = 1
print(time)
