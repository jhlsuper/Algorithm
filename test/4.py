## 최대 p명 탑승 가능

## 배 처음 A에

## 식인종의 수 > 사람  잡아먹음

## 배에 사람 or 식인종 1명 이동 꼭 이동해야됨.

## 안전하게 불가능 하면 -1
## n = 사람 m  =식인종 , p 배에타는 사람
from itertools import combinations, permutations


def solution(n, m, p):
    answer = 0
    all = []
    way = set()  ## 배에타는 가지수
    for i in range(n):
        all.append(0)
    for i in range(m):
        all.append(1)
    islandA = all
    islandB = []
    ship = []
    for i in range(0, p):

        for j in combinations(all, i + 1):
            # print(list(j))
            way.add(j)
    # print(way)

    if (len(islandB) == n + m):
        return answer


def get_sum(li):
    people = 0
    eater = 0
    for i in li:
        if i == 0:
            people += 1
        else:
            eater += 1
    if people >= eater:
        return True
    else:
        return False


solution(2, 2, 2)
