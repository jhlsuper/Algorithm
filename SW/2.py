## 2개의 직통 노선을 만든다.
## 1. 2개의 직통 노선은 교차 X
## 2. 인접한 두역은 직통 노선 X
## 3. 인접한 두역에서 출발, 인적한 두역으로 도착하는 거 X
## 4. 1개 역에서 2개의 직통 노선 X

## 타당도 가장크게 직통 노선 건설, 타당도값 구하기
##타당도 = pow(A+B) + pow(C+D)
from itertools import combinations
from copy import deepcopy

T = int(input())
for t in range(T):
    N = int(input())
    li = list(map(int, input().split(" ")))
    indexLi = []
    for i in range(N):
        indexLi.append(i)

    answer = 0

    for a, b, in combinations(indexLi, 2):
        score = 0

        if b - a == 1 or b - a == N - 1:
            continue
        temp = li[a] + li[b]
        score += pow(temp, 2)
        newIndexLi = deepcopy(indexLi)
        lineA = a
        lineB = b
        newIndexLi.remove(a)
        newIndexLi.remove(b)

        for c, d in combinations(newIndexLi, 2):
            tempscore = score
            if d - c == 1 or d - c == N - 1:
                continue
            if lineB == N - 1 and c == 0:
                continue
            if lineA == 0 and d == N - 1:
                continue
            ## 조건 1 c,d가 모두 a,b 사이일때
            if lineA + 1 < c and c + 1 < d < lineB - 1:
                temp = li[c] + li[d]
                tempscore += pow(temp, 2)
            ## 조건 2 c가 a미만,d가 b 초과일때
            if c < lineA - 1 and d > lineB + 1:
                temp = li[c] + li[d]
                tempscore += pow(temp, 2)
            ## 조건 3 c,d가 모두 a미만
            if c < d < lineA - 1:
                temp = li[c] + li[d]
                tempscore += pow(temp, 2)
            ## 조건 4 c,d가 모두 b초과
            if lineB + 1 < c < d:
                temp = li[c] + li[d]
                tempscore += pow(temp, 2)
            if tempscore > answer:
                answer = tempscore

    print(f'#{t + 1} {answer}')
