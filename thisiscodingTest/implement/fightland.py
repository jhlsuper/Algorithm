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
maps.append([0]*n)
for i in range(n):
    a = [0]
    temp = a + list(map(int, input().split()))
    # 총 안들고있다
    maps.append(temp)
for i in range(m):
    temp = list(map(int, input().split()))
    temp.append(False)
    people.append(temp)
index = 65
for i in people:
    # print(i)
    x = i[0]
    y = i[1]
    maps[x][y] = chr(index)
    index += 1
print(maps, people)


def move(people):
    x, y, d, s, g = people
    nx = x + dx[d]
    ny = y + dy[d]
    if 1 <= nx <= n and 1 <= ny <= n:
        npeople = [nx, ny, d, s, g]

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
        npeople = [nx, ny, d, s, g]
    return npeople


def checkPosition(person,n):  ##이동후에 좌표 확인 n은 people의 몇번째 사람인지
    x, y, d, s, g = person
    ## 총이있다면
    if maps[x][y] != 0 and not str(maps[x][y]).isalpha():
        if g == False:
            npeople = [x, y, d, s + maps[x][y], maps[x][y]]
            maps[x][y] = str()
            return npeople
    ## 사람이있다면
    if str(maps[x][y]).isalpha():
        op = people[ord(maps[x][y])-65]
        


## 둘다 아니라면
    if maps[x][y] ==0:
        return people

# def checkpeople(x, y):
