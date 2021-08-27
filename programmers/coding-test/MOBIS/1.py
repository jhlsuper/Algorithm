from itertools import combinations
from itertools import product
from itertools import permutations


def solution(dice):
    dict = {}
    temp_list = []
    answer = 0
    j=0
    for i in range(len(dice)):
        for
    for index in dice:
        for j in index:
            dict[j] = 1
            temp_list.append(j)
    l = len(temp_list)
    print(temp_list, l)
    case = list(map(''.join, permutations(map(str, temp_list), 2)))
    for i in case:
        dict[int(i)] = 1

    sdict = sorted(dict.items())
    print(sdict)
    dict_index = 0

    while sdict:
        if sdict[dict_index][0] + 1 == sdict[dict_index + 1][0]:

            dict_index += 1
        else:
            print(dict_index + 1)
            return dict_index + 1


solution([[0, 1, 5, 3, 9, 2], [2, 1, 0, 4, 8, 7], [6, 3, 4, 7, 6, 5]])
