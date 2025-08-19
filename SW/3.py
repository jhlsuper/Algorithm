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


def getSize(list):
    count = 0
    for i in list:
        if i == False:
            count += 1
    return count


T = int(input())  ##테스트 케이스 갯수
for t in range(T):
    answer = 0
    N = int(input())
    li = list(map(int, input().split(" ")))
    # print(li)
    visited = [False] * N

    d = deque()
    d.append((visited, 0))

    while d:
        tempLi, score = d.popleft()
        # print(tempLi, score)
        # size = len(tempLi)
        size = getSize(tempLi)
        if size == 1:
            for j in range(N):
                if tempLi[j] == False:
                    score += li[j]
                    break
            if answer < score:
                answer = score
                # break
        else:
            newTempScore = 0
            for i in range(size):

                # newTempLi = tempLi[0:i] + tempLi[i + 1:]

                if i == 0:
                    tempScore = score

                    # if tempLi[1] >= newTempScore:
                    # newTempScore = tempLi[1]
                    tempScore += li[1]
                    tempLi[i] = True
                    d.append((tempLi, tempScore))
                elif i == size - 1:
                    tempScore = score

                    tempScore += li[size - 2]
                    tempLi[i] = True
                    d.append((tempLi, tempScore))

                else:
                    tempScore = score
                    tempIndexLeft = i
                    tempIndexRight = i
                    while tempLi[tempIndexLeft] == False:
                        tempIndexLeft -= 1
                    while tempLi[tempIndexRight] == False:
                        tempIndexRight += 1
                    tempLi[i] = True
                    # if (tempLi[i - 1] * tempLi[i + 1]) > newTempScore:
                    tempScore += (li[tempIndexLeft] * li[tempIndexRight])
                    d.append((tempLi, tempScore))
    # print(answer)
    print(f'#{t + 1} {answer}')
