## N 크기의 배열
## L 명이상 R명 이하면 국경 열림

## 각칸의 인구수 연합 인구수 / 칸의 개수

## 두칸의 차이가 사이인거 전부 마킹 값 배열에 넣기 모두 더해서 나눠주기
## 나누어져 있으면 배열값에 배열로 추가
import math
from collections import deque

global visited
global answer
# global visited
global opened
N, L, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

opened = []
x, y = 0, 0
answer = 0


def bfs(a, b):
    q = deque()
    temp = []
    q.append((a, b))
    temp.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]

            if 0 <= newX < N and 0 <= newY < N and visited[newX][newY] == 0:

                if L <= abs(arr[x][y] - arr[newX][newY]) <= R:
                    visited[newX][newY] = 1
                    q.append((newX, newY))
                    temp.append((newX, newY))

    return temp


while 1:
    visited = [[0] * (N + 1) for _ in range(N + 1)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)
                if len(country) > 1:
                    flag = 1
                    number = sum([arr[x][y] for x, y in country]) // len(country)
                    for x, y in country:
                        arr[x][y] = number
    if flag == 0:
        break
    answer += 1

print(answer)
