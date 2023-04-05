T = int(input())

global people
global index
global N
global B
global min


def dfs(i, s):
    global min
    global people
    global B
    # print(s, B, min)
    ##종료조건
    if B <= s < min:
        min = s
        # print(min, "min")
    if i == N + 1:
        return

    if s > min:
        return
    dfs(i + 1, s)
    dfs(i + 1, s + people[i - 1])


for tc in range(1, T + 1):
    answer = 0
    N, B = map(int, input().split())
    people = list(map(int, input().split()))
    sum = 0
    min = 9999999
    dfs(1, sum)

    print(f'#{tc} {min-B}')
