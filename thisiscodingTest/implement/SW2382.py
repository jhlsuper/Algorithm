# 각 군집들은 1시간마다 이동방향에 있는 다음 셀로 이동한다.


# 미생물 군집이 이동 후 약품이 칠해진 셀에 도착하면 군집 내 미생물의 절반이 죽고, 이동방향이 반대로 바뀐다.
#       미생물 수가 홀수인 경우 반으로 나누어 떨어지지 않으므로, 다음과 같이 정의한다.
#       살아남은 미생물 수 = 원래 미생물 수를 2로 나눈 후 소수점 이하를 버림 한 값
#       따라서 군집에 미생물이 한 마리 있는 경우 살아남은 미생물 수가 0이 되기 때문에, 군집이 사라지게 된다,


#  이동 후 두 개 이상의 군집이 한 셀에 모이는 경우 군집들이 합쳐지게 된다.
#  합쳐 진 군집의 미생물 수는 군집들의 미생물 수의 합이며, 이동 방향은 군집들 중 미생물 수가 가장 많은 군집의 이동방향이 된다.
#  합쳐지는 군집의 미생물 수가 같은 경우는 주어지지 않으므로 고려하지 않아도 된다.


dx = [0, -1, 1, 0, 0]  ##상하 좌우
dy = [0, 0, 0, -1, 1]


def move(micros):
    temp = []
    for m in micros:
        x, y, c, d = m
        nx, ny, nc, nd = x, y, c, d
        # print(x, y, c, d)
        if (x == 1 and d == 1) or (x == N - 2 and d == 2) or (y == 1 and d == 3) or (
                y == N - 2 and d == 4):  ##끝으로 이동할 때
            nx = x + dx[d]
            ny = y + dy[d]
            if d == 1:
                nd = 2
            elif d == 2:
                nd = 1
            elif d == 3:
                nd = 4
            elif d == 4:
                nd = 3
            if c == 1:
                nc = 0
            else:

                nc = c // 2
            # maps[x][y].remove((c, d))
            # maps[nx][ny].append((nc, nd))
        else:
            nx = x + dx[d]
            ny = y + dy[d]

            # maps[x][y].remove((c, d))
            # maps[nx][ny].append((nc, d))
        # print(nx, ny, nc, nd)
        temp.append((nx, ny, nc, nd))
        # micros.remove((x, y, c, d))
        # micros.append((nx, ny, nc, nd))
        # print(nx,ny,nc,nd)
    return temp


T = int(input())

for tc in range(T):

    N, M, K = map(int, input().split())  # N 셀의 갯수 , M 격리 시간 ,K 미생물의 갯수
    maps = [[[]] * N for _ in range(N)]

    micro = []
    for i in range(K):
        x, y, c, d = map(int, input().split())
        micro.append((x, y, c, d))
        # maps[x][y].append((c, d))

    print(micro)
    micro = move(micro)
    print(micro)
