def sublist_max(profits):
    # 코드를 작성하세요.
    # brute force를 이용하려면 전수 조사를 해야된다. 전수조사를 할려면
    # 리스트의 0번째 원소 0,1/01,2부터 끝까지 1번째 , 1,2/부터 끝까지 다해봐야함
    sub_max = 0

    for i in range(len(profits)):
        for j in range(len(profits)):
            sub_max = max(sub_max, sum(profits[i:i+j+1]))

    return sub_max

    # 코드잇의 해법
    # for i in range(len(profits)):
    #     #인덱스 i부터 j까지 수익의 합을 보관
    #     total = 0
    #     for j  in range(i, len(profits)):
    #         total += profits[j]

    #         max_profit = max(max_profit,total)
    # return max_profit


print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))
