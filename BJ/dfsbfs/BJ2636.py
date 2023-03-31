import sys

N, M = map(int, input().split())

## N세로 , M 가로
maps = [list(map(int, input().split())) for _ in range(N)]

print(maps)
