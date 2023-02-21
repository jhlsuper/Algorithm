## N 크기의 배열
## L 명이상 R명 이하면 국경 열림

## 각칸의 인구수 연합 인구수 / 칸의 개수

## 두칸의 차이가 사이인거 전부 마킹 값 배열에 넣기 모두 더해서 나눠주기
## 나누어져 있으면 배열값에 배열로 추가
global visited
global answer
global visited
global opened
N, L, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

visited = []
opened = []
x, y = 0, 0
answer = 0
flag = True


def dfs(x, y):
    print(opened)
    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]

        if 0 <= newX < N and 0 <= newY < N:

            if L <= abs(arr[x][y] - arr[newX][newY]) <= R:
                opened.append((newX, newY))
            if (newX, newY) not in visited:
                visited.append((newX, newY))
                dfs(newX, newY)


def move():
    sum = 0
    global answer
    if len(opened) > 0:
        answer += 1
        for a, b in opened:
            sum += arr[a][b]

        each = int(sum / len(visited))
        for a, b in opened:
            arr[a][b] = each
        opened.clear()
        visited.clear()
        return True
    else:
        return False


# while flag:
dfs(0, 0)
print(arr)
move()
print(arr)

print(answer)
