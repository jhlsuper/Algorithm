## N개의 풍성  1~10개
## N개의 총알 N번 쏘기
## 터지고 나면 일정한 간격으로 이동
## 획득 점수 = 경품

##점수 0점
## 1. 풍성 터지면 left * right 점수
## 2. left or right만 있으면 그 점수
## 3. left or right 둘다 없으면 풍선 숫자.
## 최대 점수를 계산하는 프로그램!!

from collections import deque

T = int(input())  ##테스트 케이스 갯수
for t in range(T):
    answer = 0
    N = int(input())
    li = list(map(int, input().split(" ")))
    # print(li)
    visited = [False] * N

    d = deque()
    d.append((li, 0))

    while d:
        tempLi, score = d.popleft()
        # print(tempLi, score)
        size = len(tempLi)

        if size == 1:

            score += tempLi[0]
            if answer < score:
                answer = score
                # break
        else:
            newTempScore = 0
            for i in range(size):

                # newTempLi = tempLi[0:i] + tempLi[i + 1:]

                if i == 0:
                    tempScore = score

                    if tempLi[1] >= newTempScore:
                        newTempScore = tempLi[1]
                        tempScore += tempLi[1]
                        d.append((tempLi[0:i] + tempLi[i + 1:], tempScore))
                elif i == size - 1:
                    tempScore = score
                    if tempLi[size - 2] >= newTempScore:
                        newTempScore = tempLi[size - 2]
                        tempScore += tempLi[size - 2]
                        d.append((tempLi[0:i] + tempLi[i + 1:], tempScore))

                else:
                    tempScore = score
                    if (tempLi[i - 1] * tempLi[i + 1]) > newTempScore:
                        tempScore += (tempLi[i - 1] * tempLi[i + 1])
                        d.append((tempLi[0:i] + tempLi[i + 1:], tempScore))
    # print(answer)
    print(f'#{t + 1} {answer}')
