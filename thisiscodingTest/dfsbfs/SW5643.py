from collections import deque

T = int(input())

for ic in range(T):
    N = int(input())  # node의 수
    M = int(input())  # edge의 수
    answer = 0
    maps = [[0] * (N + 1) for _ in range(N + 1)]
    check = [0] * (N + 1)
    for i in range(M):
        x, y = map(int, input().split())
        check[x] +=1
        maps[x][y] = 1

    print(maps, check)