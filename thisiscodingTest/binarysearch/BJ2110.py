## N개의 집
## C개의 공유기
## 인접한 두 공유기 사이의 거리를 가능한 크게  거리를 최대로

import sys

input = sys.stdin.readline

result =0
def binary_search(house_pos, num):
    global result
    start = 1
    end = house_pos[-1] - house_pos[0]

    while start <= end:
        mid = (start + end) // 2
        position = house_pos[0]
        count = 1
        for i in range(1, len(house_pos)):
            if house_pos[i] >= position + mid:
                count += 1
                position = house_pos[i]
        if count >= num:
            start = mid + 1
            result = mid
        else:
            end = mid - 1



N, C = (map(int, input().split()))

arr = [int(input().rstrip()) for _ in range(N)]
arr = sorted(arr)
binary_search(arr, C)
print(result)
