## 수욜의 원소 중에서 그 값이 인덱스와 동일한 원소

def binary_search(li, start, end):
    if start > end:
        return False
    mid = (start + end) // 2

    if li[mid] == mid:
        return mid
    elif li[mid] > mid:
        return binary_search(li, start, mid - 1)
    else:
        return binary_search(li, mid + 1, end)


N = int(input())
li = list(map(int, input().split()))

answer = binary_search(li, 0, N - 1)
if answer != False:
    print(answer)
else:
    print(-1)
