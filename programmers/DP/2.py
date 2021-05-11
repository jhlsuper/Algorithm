def solution(triangle):
    answer = 0
    dp = []

    for i in (triangle):
        list = []
        if len(dp) == 0:
            list.append(i[0])
        else:
            for index, num in enumerate(i):
                if index == 0:
                    list.append(dp[-1][index]+num)
                elif index == len(i)-1:
                    list.append(dp[-1][-1]+num)
                else:
                    list.append(max(dp[-1][index-1], dp[-1][index])+num)
        dp.append(list)

        # print(i)
    print(max(dp[-1]))
    return max(dp[-1])


solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
