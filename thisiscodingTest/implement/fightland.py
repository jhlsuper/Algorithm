## 싸움땅 문제
##n*n 크기의 격자에서 진행
import sys

dx = [-1, 0, 1, 0]  # 상 우 하 좌
dy = [0, 1, 0, -1]
input = sys.stdin.readline
## n, m k  격자의 크기 , 플레이어의 수 , 라운드 수
n, m, k = map(int, input().split())
maps = []
people = []
point = [0] * m
hmaps = []  ## 사람의 좌표가 적혀있는 지도

maps.append([0] * (n + 1))
for i in range(n + 1):
    hmaps.append([0] * (n + 1))

for i in range(n):
    a = [0]
    temp = a + list(map(int, input().split()))
    # 총 안들고있다
    maps.append(temp)
index = 65
for i in range(m):
    temp = list(map(int, input().split()))
    temp.append(False)
    temp.append(chr(index + i))

    people.append(temp)
    hmaps[temp[0]][temp[1]] = temp[-1]
# print(hmaps)
# for i in people:
#     # print(i)
#     x = i[0]
#     y = i[1]
#     maps[x][y] = chr(index)
#     index += 1
print(maps, people)
print(hmaps)


def move(people):
    x, y, d, s, g, i = people
    nx = x + dx[d]
    ny = y + dy[d]
    # hmaps[x][y] = 0
    if 1 <= nx <= n and 1 <= ny <= n:
        npeople = [nx, ny, d, s, g, i]
        # maps[nx][ny] = i
    else:
        if d == 0:
            nx = x + dx[2]
            ny = y + dy[2]

        if d == 1:
            nx = x + dx[3]
            ny = y + dy[3]
        if d == 2:
            nx = x + dx[0]
            ny = y + dy[0]
        if d == 3:
            nx = x + dx[1]
            ny = y + dy[1]
        # maps[nx][ny] = i
        npeople = [nx, ny, d, s, g, i]
    return npeople


def checkPosition(person):  ##이동후에 좌표 확인 n은 people의 몇번째 사람인지
    x, y, d, s, g, i = person

    ## 총이있다면
    if maps[x][y] != 0 and not (hmaps[x][y]).isalpha():
        if g == False:
            npeople = [x, y, d, s + maps[x][y], maps[x][y], i]
            maps[x][y] = i
            return npeople
    # 사람이있다면
    if (hmaps[x][y]).isalpha():
        op = people[ord(hmaps[x][y]) - 65]  ## 상대방
        xo, xo, do, so, go, io = op
        if s > so:  ##이동한 사람이 이김
            point[ord(i) - 65] += s - so
            maps[x][y] = go
           ##총바꾸는거 구현

        if s == so:  ##둘의 능력치가 같으면
            print("같아")
        if s < so:  ##원래 있던 사람이 이김
            point[ord(io) - 65] += so - s

    ## 둘다 아니라면
    if maps[x][y] == 0:
        return people


# def checkpeople(x, y):

for i in range(k):
    for p in range(len(people)):
        move(people[p])
        # checkPosition(people[p])
print(maps)
