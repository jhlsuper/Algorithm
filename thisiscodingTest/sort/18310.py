N = int(input())

answer = 1e9
li = list(map(int, input().split()))
# print(li)
# print(sorted(li))
li = sorted(li)
if len(li) != 1:
    length = li[-1] - li[0]

# print(int(length / 2))
mid = int(length / 2) + li[0]
if mid in li:
    answer = mid
    print(answer)
else:

    while True:
        mid_up = mid + 1
        mid_down = mid - 1
        print(mid_down, mid_up)
        if mid_down in li:
            answer = mid_down
            break
        if mid_up in li:
            # print(mid_up, mid_down)
            answer = mid_up
            break
    print(answer)


def getDiff(a):
    temp = 0
    for i in li:
        temp += abs(a - i)
    return temp
