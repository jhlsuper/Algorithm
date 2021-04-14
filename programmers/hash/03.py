from typing import Dict


def solution(clothes):
    dictionary = {}
    gop = 1

    for i in clothes:
        if i[-1] in dictionary:
            dictionary[i[-1]] += 1
        else:
            dictionary[i[-1]] = 1
    # print(dictionary)
    for val in dictionary.values():
        gop *= val+1

    return gop-1  # 전부 안입는 경우를 뺀다.


solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"],
          ["green_turban", "headgear"]])
