import heapq

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
t = int(input())
for _ in range(t):
    n = int(input())
    INF = int(1e9)
    map = []

    for _ in range(n):
        map.append(list(map(int, input().split())))
    dis = [[INF] * n for _ in range(n)]
    q = []
    while q:
        dist, x, y = heapq.heappop(q)
        if dist > dis[x][y]:
            continue
        for i in range(4):
            newX, newY = x + dx[i], y + dy[i]
            if newX < 0 or newX >= n or newY < 0 or newY >= n:
                continue
            cost = dist + map[newX][newY]
            if cost < dis[newX][newY]:
                dis[newX][newY] = cost
                heapq.heappush(q, (cost, newX, newY))
    print(dis[n - 1][n - 1])
