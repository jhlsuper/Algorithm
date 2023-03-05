n, m = map(int, input().split())
INF = int(1e9)
answer = 0
map = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(1, n + 1):
    i, j = map(int, input().split())
    map[i][j] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            map[a][b] = min(map[a][b], map[a][k] + map[k][b])]

for i in range(1, n + 1):
    flag = True
    for j in range(1, n + 1):
        if map[i][j] == map[j][j] == INF:
            flag = False
            break
    if flag:
        answer += 1
print(answer)

##
