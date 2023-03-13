## M : N
from collections import deque
;
dx = [-1, 0, 0, 1]  ## 상 좌 우 하
dy = [0, -1, 1, 0]
N, M = map(int, input().split())
shop = []  # 편의점 좌표값
basecamp = deque()  ## 베이스 캠프 좌표값 가고싶어하는
answer = 0  # 지난 시간
people = []  ##map에 올라와있는 사람의 값
maps = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            basecamp.append([i, j])

for i in range(M):
    a, b = map(int, input().split())
    shop.append([a, b])

print(shop, basecamp, maps)


# 3단계가 있습니다.
# 1 단계 상 좌 우 하 방향 이동
# 최단 거리로 이동

## 2단계
## if 편의점 위치 -> 편의점좌표값 3? --> can not pass

### 3단계 
### t초에 t번 사람은 편의점에서 가장 가까운 베이스 켐프로 이동
### 행이 같다면 열이 작은 베이스 캠프 사람이 들어간 베이스 캠프는
### 그곳으로 이동 불가  (2,1) 보다 (2,5)

# while True:


def step1():
    if len(basecamp) != 0:
        # temp = basecamp.popleft()
        people.append(basecamp.popleft()) ##이 좌표값은 베이스캠프
    else:

        for i in people:
            move(i[0], i[1])


def step3():


def findShortestWay(x, y):  ##가장 가까운 베이스캠프를 구한다.
    for i in range(basecamp)
def move(x, y):  ##가장 가까운 우선순위를 고려해서 한칸 이동한다.
