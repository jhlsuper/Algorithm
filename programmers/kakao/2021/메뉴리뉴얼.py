from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for n in course:
        array = []
        for o in orders:
            order = sorted(o)
            # print(list(combinations(order, n)))
            array.extend(list(combinations(order, n)))

        count = Counter(array).most_common()

        for index in range(len(count)):
            temp_max = count[0][1]
            if count[index][1] >= 2 and count[index][1] == temp_max:
                answer.append("".join(count[index][0]))
            else:
                break

    return sorted(answer)


solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])
