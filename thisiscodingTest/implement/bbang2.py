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

## 편의점
store = [list(map(int, input().strip().split())) for _ in range(m)]

##방문 할 수 있는지 확인
check = [[0 for _ in range(n + 1)] for _ in range(n + 1)]


# 편의점과 베이스의 거리
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


# 편의점에서 가장 가까운 베이스 구하기
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


# 사람 to 편의점 최단거리 루트 찾기
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
        return sys.maxsize, 0, 0  ##방문 못하면거리 max값 ㄱㄷ셔구
    while q:
        px, py = q.popleft()
        if px == sx and py == sy:  ##편의점 도착시 거리, x,y 반환
            return visited[px][py] - 1, fnx, fny
        for i in range(4):
            nx, ny = px + dx[i], py + dy[i]

            if 1 <= nx < n + 1 and 1 <= ny < n + 1 and not check[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = visited[px][py] + 1
                q.append((nx, ny))
    return sys.maxsize, 0, 0


poslist = [[] for _ in range(m)]  ##사람별 현재 위치
time = 1  ##흐른 시간

sx, sy = store[0]
bx, by = findbase(sx, sy)
poslist[0] = [bx, by]
check[bx][by] = 1  ## 방문 못하는 곳으로 check

stop = [0 for _ in range(m)]  # 1이면 도착완료
count = 0  # 도착한 사람 수 ㄴ
while count < m:
    time += 1
    tempgo = [(0, 0) for _ in range(m)]  ##다음 위치
    for i in range(m):
        if poslist[i] and not stop[i]:
            sx, sy = store[i]
            x, y = poslist[i]
            min_dis = sys.maxsize
            minfx, minfy = 0, 0

            for d in range(4):  ##4가지 방형으로 거리 구하기 최단거리인 방향 구하기
                dis, fx, fy = gotostore(x, y, sx, sy, d)
                if min_dis > dis:
                    min_dis = dis
                    minfx, minfy = fx, fy
            tempgo[i] = (minfx, minfy)
    for i, (fx, fy) in enumerate(tempgo):  ## 도착지에 도착한 경우
        if store[i][0] == fx and store[i][1] == fy:
            poslist[i] = [fx, fy]
            check[fx][fy] = 1
            stop[i] = 1
            count += 1
        else:  ## 이동
            poslist[i] = [fx, fy]
    if time <= m:
        bx, by = findbase(store[time - 1][0], store[time - 1][1])
        poslist[time - 1] = [bx, by]
        check[bx][by] = 1
print(time)
