# R*C
# 폭탄 3초뒤 폭발 - 4방도 같이 터짐 , 연쇄 폭팔 x
# 봄버맨 모든 칸 이동 가능
# 폭탄 init()
# 1초 pause
# 1초동안 폭탄없는 모든 칸에 폭탄 설치
# 1초가 지난 후에 3초전에 설치된 폭탄 폭발

# N초가 흐른후의 격체 상태를 구하라
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

global bombs

time = 0


def putBomb():
    global bombs
    temp = []
    for x, y, c in bombs:
        temp.append([x, y, c + 1])

    for i in range(R):
        for j in range(C):
            if maps[i][j] == '.':
                maps[i][j] = 'O'
                temp.append([i, j, 0])
    bombs = temp


def oneSec():
    global bombs
    temp = []
    for x, y, c in bombs:
        temp.append([x, y, c + 1])
    bombs = temp


def popBomb():
    poplist = set()
    realPopList = set()
    for x, y, c in bombs:
        if c == 3:
            poplist.add((x, y))
    # print(poplist)
    for x, y, in poplist:
        realPopList.add((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                realPopList.add((nx, ny))
    # print(realPopList)
    for x, y in realPopList:
        maps[x][y] = '.'
    findBombs()


def findBombs():
    for i in range(R):
        for j in range(C):
            if maps[i][j] == 'O':
                bombs.append([i, j, 1])


R, C, N = map(int, input().split())
bombs = []
maps = [list(input()) for _ in range(R)]
for i in range(R):
    for j in range(C):
        if maps[i][j] == 'O':
            bombs.append([i, j, 1])

    # putBomb()
    # print(maps, bombs)
    # oneSec()
    # print(maps, bombs)
    # popBomb()
    # print(maps)
oneSec()
time += 1
# print(maps, bombs)
while time < N:
    # oneSec()
    putBomb()
    print(maps, bombs)

    popBomb()

    time += 1

for i in range(R):
    for j in range(C):
        print(maps[i][j], end="")
    print()
