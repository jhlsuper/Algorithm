from collections import deque

##로봇 길이 2개
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
global arr
global size
global visited


def solution(board):
    arr = board
    answer = 0
    size = len(board[0])
    return answer


## 0이면 가로 1이면 세로
def dfs(x1, y1, x2, y2, dir):
    q = deque
    temp = []
    q.append((x1, y1, x2, y2, dir))
    temp.append(x1, y1, x2, y2, dir)
    ##상하좌우 이동
    for i in range(5):
        ##시계방향 회전
        if i == 4:
            if dir == 0:
                if 0 <= y1 + 1 < size and 0 <= y2 + 1 < size:
                    newX1 = x1
                    newY1 = y1 + 1
                    newX2 = x2
                    newY2 = y2 + 1
            else:
                if
            ##반시계방향 회전 없다고 가정

        else:

            newX1 = x1 + dx[i]
            newY1 = y1 + dy[i]
            newX2 = x2 + dx[i]
            newY2 = y2 + dy[i]
        if 0 <= newX1 < size and 0 <= newY1 < size and 0 <= newX2 < size and 0 <= newY2 < size and visited[newX2][
            newY2] == 0:
            visited[newX2][newY2] = 1
            q.append((newX1, newY1, newX2, newY2))
    return temp


solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]])
