def solution(N, stages):
    answer = []
    ## N , 스테이지 갯수
    li = [0] * (N + 1)  ## 도달한 사람
    notlist = [0] * (N + 1)  ## 클리어 못한 사람

    for i in stages:
        if i == N + 1:

            # for j in range(i):
            li[i-1] += 1

            # notlist[i - 1] += 1
        else:
            for j in range(i):
                li[j] += 1
            notlist[i] += 1
    print(li, notlist)
    for i in range(1, N + 1):
        # print(notlist[i] / li[i])
        if li[i]==0 :
            answer.append((i,0))
        else:

            answer.append((i, notlist[i] / li[i]))
    print(answer)
    return answer


solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
