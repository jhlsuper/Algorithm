import sys
from itertools import combinations

def checkD(maps, k):
    totalCnt = 0
    for i in range(w):

        ##0이면 A 1이면 B
        flag = maps[0][i]
        count = 1
        for j in range(1, d):
            index = maps[j][i]
            if index == flag:
                count += 1
            else:
                flag = index
                count = 1
            if count >= k:
                totalCnt += 1
                break
    if totalCnt == w:
        return True
    else:
        return False


T = int(input())
global d
global w
global k
for tc in range(T):
    d, w, k = map(int, input().split())
    ## 두께 w 가로크기
    maps = [list(map(int, input().split())) for _ in range(d)]
    print( checkD(maps, k))
    # print(maps)
    if checkD(maps,k):
        print(f"#{tc+1} 0")
    else:
        indexli =[]
        for i in range(d):
            indexli.append(i)
        for i in range(1,d):
            for c in combinations(indexli, i):
                for a in c:
