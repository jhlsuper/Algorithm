import math

n, m, k, c, = map(int, input().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

tx = [-1, 1, -1, 1]  # 대각선
ty = [-1, -1, 1, 1]
maps = []
trees = []
empty = []


# print(maps)
def grow():  # 나무 성장 이게 지금 동작 x
    global maps
    global trees
    for x, y in trees:
        count = 0
        for i in range(4):
            # print(i)
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # print(nx,ny)
                if maps[nx][ny] > 0:
                    count += 1
        print(count)
        maps[x][y] += count


def findEmptyAndTrees():
    global maps
    global empty
    global trees
    empty = []
    trees = []
    for i in range(n):
        for j in range(n):
            if maps[i][j] > 0:
                trees.append((i, j))
            if maps[i][j] == 0:
                empty.append((i, j))


def reproduce():
    for x, y in trees:
        count = 0
        temp = []
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx, ny) in empty:
                count += 1
                temp.append((nx, ny))
        print(count, x, y)
        if count > 0:
            for i, j in temp:
                maps[i][j] += int(maps[x][y] // count)
                print(maps[x][y], (maps[x][y] // count))
    findEmptyAndTrees()


def findBiggestKill():
    biggest = 0
    kx, ky = 0, 0
    for x, y in trees:
        # count = 0
        count = maps[x][y]
        print("-----", x, y)
        for i in range(4):
            for j in range(1, k + 1):

                nx = x + (tx[i] * j)
                ny = y + (ty[i] * j)
                if 0 <= nx < n and 0 <= ny < n:
                    if maps[nx][ny] > 0:
                        count += maps[nx][ny]
                        print(nx, ny, maps[nx][ny])
                    else:
                        break
        print(count)
        if count > biggest:
            biggest = count
            kx = x
            ky = y
    print(kx, ky)


for i in range(n):
    temp = list(map(int, input().split()))
    maps.append(temp)
    # for j in range(n):
    #     if temp[j] > 0:
    #         trees.append((i, j))

# print(maps)
findEmptyAndTrees()
grow()
reproduce()
print(trees)
findBiggestKill()
