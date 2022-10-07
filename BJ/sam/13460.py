from collections import deque
import sys 

input = sys.stdin.readline

n, m = map(int, input().split())
graph =[]

for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] =='R':
            rx, ry = i,j 
        elif graph[i][j] =='B':
            bx, by = i,j 

dx =[-1,1,0,0]
dy = [0,0,-1,-1]

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by))
    count =0
    while q:
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()
            if(count)