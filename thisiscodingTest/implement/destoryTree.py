n, m, k, c, = map(int, input().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

tx = [-1, 1, -1, 1]  # 대각선
ty = [-1, -1, 1, 1]
maps = []
trees = []
empty = []
killer = []  # 제초제 좌표 남은 일수
answer = 0


# print(maps)
def grow():
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
        # print(count)
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
        # print(count, x, y)
        if count > 0:
            for i, j in temp:
                maps[i][j] += int(maps[x][y] // count)
                # print(maps[x][y], (maps[x][y] // count))
    findEmptyAndTrees()


def findBiggestKill():
    biggestList = []
    global answer
    biggest = 0
    kx, ky = 0, 0
    for x, y in trees:
        # count = 0
        count = maps[x][y]
        # print("-----", x, y)
        for i in range(4):
            for j in range(1, k + 1):

                nx = x + (tx[i] * j)
                ny = y + (ty[i] * j)
                if 0 <= nx < n and 0 <= ny < n:
                    if maps[nx][ny] > 0:
                        count += maps[nx][ny]
                        # print(nx, ny, maps[nx][ny])
                    else:
                        break
        # print(count)
        if count > biggest:
            biggest = count
            kx = x
            ky = y
        if count == biggest:
            if x < kx:
                kx = x
                ky = y
                biggest = count
            elif x == kx:
                if y < ky:
                    kx = x
                    ky = y
                    biggest =count
            # biggestList.append((x, y, biggest))
    answer += biggest
    # for x,y,biggest in biggestList:
    # sorted(biggestList, key=lambda big: (big[0], big[1]))
    # answer += biggestList[0][2]
    # kx = biggestList[0][0]
    # ky = biggestList[0][1]
    return kx, ky


def sprayKiller(x, y):  ## 제초제 뿌리기
    global answer
    # answer += maps[x][y]
    maps[x][y] = (-5)
    killer.append([x, y, c])
    for i in range(4):
        for j in range(1, k + 1):
            nx = x + (tx[i] * j)
            ny = y + (ty[i] * j)
            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] > 0:
                    # answer += maps[nx][ny]
                    maps[nx][ny] = (-5)

                    killer.append([nx, ny, c])
                    # print(nx, ny, maps[nx][ny])

                else:
                    if maps[nx][ny] == -1:
                        break
                    if maps[nx][ny] == 0:
                        maps[nx][ny] = (-5)
                        killer.append([nx, ny, c])
                        break
                    else:
                        # answer += maps[nx][ny]
                        for idx in range(len(killer)):
                            a, b, c1 = killer[idx]
                            if nx == a and ny == b:
                                killer[idx] = [a, b, c]
                                break
                        maps[nx][ny] = (-5)

                        # killer.append([nx, ny, c])
                        # break


def oneYear():
    global killer
    temp = []
    for i in range(len(killer)):
        # print(x, y, c)
        x, y, c = killer[i][0], killer[i][1], killer[i][2]
        if c == 1:
            maps[x][y] = 0
        else:
            temp.append([x, y, c - 1])
    killer = temp
    findEmptyAndTrees()


for i in range(n):
    temp = list(map(int, input().split()))
    maps.append(temp)


# print(maps)


def firstyear():
    findEmptyAndTrees()
    grow()
    reproduce()
    x, y = findBiggestKill()
    sprayKiller(x, y)


def year():
    grow()
    reproduce()
    oneYear()
    x, y = findBiggestKill()
    sprayKiller(x, y)


for i in range(1, m + 1):
    if i > 1:
        year()
        print(maps)
    else:
        firstyear()
        print(maps)
print(answer)
