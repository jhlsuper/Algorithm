from typing import Dict


def solution(n, z, roads, queries):
    answer = []
    min_point = 1000
    position = 0
    dict = {}
    can_calc = []
    dict_keys = []
    for i in roads:
        can_calc.append(i[-1])
        # print(i[-1])
        dict[i[2]] = i[1]

        min_point = min(i[-1], min_point)
    # print(dict)
    # print(min_point)
    for k in dict.keys():
        dict_keys.append(k)

    for i in range(len(dict_keys)-1):
        for j in range(1, len(dict_keys)):
            can_calc.append(dict_keys[i]+dict_keys[j])
    print(can_calc)

    for i in queries:
        if i == 0:
            if position == 0:
                answer.append(0)
        elif i < min_point:
            answer.append(-1)
        else:
            if i not in can_calc:
                answer.append(-1)

                # elif i+1 == 2:
                # print(answer)
                # return answer
    return answer


solution(5, 5, [[1, 2, 3], [0, 3, 2]], [0, 1, 2, 3, 4, 5, 6])
