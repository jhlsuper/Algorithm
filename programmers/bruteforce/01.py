def solution(answers):
    answer = []
    i = 0
    list1 = [0, 0, 0]

    lost1 = [1, 2, 3, 4, 5]
    lost2 = [2, 1, 2, 3, 2, 4, 2, 5]
    lost3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):

        print("%d, and %d " & (i % 5), answers[i])
        if lost1[i % 5] == answers[i]:

            list1[0] = +1
        if lost2[i % 8] == answers[i]:
            list1[1] += 1
        if lost3[i % 10] == answers[i]:
            list1[2] += 1
    print(list1)
    max1_index = list1.index(max(list1))

    answer.append(max1_index)
    max1 = max(list1)
    del list1[max1_index]
    if (max(list1) == max1):
        max2 = max(list1)
        max2_index = list1.index(max(list1))+1
        answer.append(max2_index)
        del list1[max2_index]
        if(max2_index == 3):
            return answer
        elif(max(list1) == max1):
            max3_index = list1.index(max(list1))+2
            return answer
    else:
        return answer

        # print((list1.index(max(list1))))

    # return answer
solution([1, 2, 3, 4, 5])
