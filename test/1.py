## 각팀에 속한 몸무게 총합 같아야함

## 최대한 많은 선수가 줄다리기 참가

## 적어도 한사람

## return 선수 선발된 모든 수 , 한팀의 무게합 (배열 )
from itertools import combinations, permutations


def solution(weight):
    answer = []
    max = 0
    max_people = 0
    li = []

    all = set()
    for i in range(0, len(weight)):
        li.append(i)
        for z in range(0, len(li)):
            for j in combinations(li, z):
                all.add((j))
    for i in all:
        for j in all:
            li_i = list(i)
            li_j = list(j)
            if is_in(li_i, li_j) and li_j and li_i:

                sum_i = get_sum(li_i, weight)
                sum_j = get_sum(li_j, weight)
                if sum_i == sum_j:
                    if sum_i > max:
                        max = sum_i
                    if (len(li_i) + len(li_j) > max_people):
                        max_people = len(li_i) + len(li_j)

    answer.append(max_people)
    answer.append(max)
    return answer


def is_in(a, b):
    flag = True
    for i in a:
        if i in b:
            flag = False
    return flag


def get_sum(i, weight):
    a = 0

    for idx in i:
        a += weight[idx]

    return a


solution([100, 60, 40, 20, 35, 45])
solution([90, 40, 50, 90])
