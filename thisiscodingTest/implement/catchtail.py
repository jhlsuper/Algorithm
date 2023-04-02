from copy import deepcopy

n, m, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

# 길
tracks = [[0] * n for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def start():
    nmaps = deepcopy(tracks)
    for team in teams:
        for index, pos in enumerate(team):
            x = pos[0]
            y = pos[1]
            if index == 0:

                nmaps[x][y] = 1
            elif index == len(team) - 1:
                nmaps[x][y] = 3
            else:
                nmaps[x][y] = 2
    return nmaps


def settrack(x, y, visited):
    visited[x][y] = True
    tracks[x][y] = 4
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and 1 <= maps[nx][ny] <= 4:
            settrack(nx, ny, visited)


def getteam(x, y, team):
    team.append([x, y])
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and 1 <= maps[nx][ny] <= 3 and [nx, ny] not in team:
            if maps[x][y] == 1 and maps[nx][ny] != 2:
                continue
            getteam(nx, ny, team)


def move(team):
    result = []
    hx, hy = team[0]
    for i in range(4):
        nx = hx + dx[i]
        ny = hy + dy[i]
        if 0 <= nx < n and 0 <= ny < n and (maps[nx][ny] == 3 or maps[nx][ny] == 4):
            result.append([nx, ny])  # head위
    team.insert(0, (hx, hy))
    # lpos = team[0]
    #
    # for i in range(1, len(team)):
    #     ni, nj = lpos
    #     result.append([ni, nj])
    #     lpos = team[i]
    return result


def getshot(r):
    shot = []  # 공의 루트
    side, p = divmod(r, n)  # 나누기 나머지
    if side % 4 == 0:
        for i in range(n):
            shot.append((p, i))
    elif side % 4 == 1:
        for i in range(n - 1, -1, -1):
            shot.append((i, p))
    elif side % 4 == 2:
        for i in range(n - 1, -1, -1):
            shot.append((n - p - 1, i))
    elif side % 4 == 3:
        for i in range(n):
            shot.append((i, n - p - 1))
    print(shot)
    return shot


def throw(shot, teams):
    for tpos in shot:
        for i in range(len(teams)):
            for idx, pos in enumerate(teams[i]):
                if tuple(pos) == tpos:
                    teams[i] = teams[i][::-1]
                    return (idx + 1) * (idx + 1)
    return 0


teams = []
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j] and 1 <= maps[i][j] <= 4:
            settrack(i, j, visited)
        if maps[i][j] == 1:
            team = []
            tempteam = getteam(i, j, team)

            teams.append(team)
    # print(teams)
score = 0
for t in range(k):
    for i in range(len(teams)):
        teams[i] = move(teams[i])
    shot = getshot(t)
    # print(shot)
    score += throw(shot, teams)
    maps = start()
print(score)
