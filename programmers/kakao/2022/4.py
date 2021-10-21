def solution(n, info):
    answer = []
    a_score = 0
    b_score = 0
    b_list = [0 for i in range(11)]
    index = n

    for j in range(11):
        if index > 0:

            if info[j] == 1 and index >= 2:
                b_list[j] += 2
                index -= 2
            elif info[j] == 0:
                b_list[j] += 1
                index -= 1
    if index != 0:
        b_list[-1] += index

    for i in range(0, 10):
        if info[i] != 0 or b_list[i] != 0:
            if info[i] >= b_list[i]:
                a_score += (10 - i)
            else:
                b_score += (10 - i)


    if a_score >= b_score:
        return [-1]
    # print(b_list)
    return b_list


solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])
