# def solution(food_times, k):
#     answer = 0
#     total = sum(food_times)
#     if (total < k):
#         return -1
#     le = len(food_times)
#     cycle = k // le
#     k = k - (le * cycle)
#     if (k == 0):
#         k += 1
#     food_times = [x - cycle for x in food_times]
#     # print(food_times)
#     # print(get_answer(0, 5), get_answer(1, 5), get_answer(2, 5), get_answer(3, 5), get_answer(4, 5))
#
#     while (True):
#         for i in range(le):
#             if (food_times[i] > 0):
#                 k -= 1
#                 food_times[i] -= 1
#                 if (k == 0):
#                     # print(get_answer(i, le))
#                     return get_answer(i, le)
#
#             elif (food_times[i] < 0):
#                 food_times[i + 1] += abs(food_times[i])
#                 food_times[i] = 0
#
#                 # for i in food_times:
#     #     sum+=i
#     # answer = sum-k
#     # return answer
#
#
# def get_answer(a, le):
#     if (a + 1 == le):
#         return 1
#     else:
#         return a + 2


def solution(food_times, k):
    answer = 0
    if (sum(food_times) <= k):
        return -1
    le = len(food_times)
    cycle = k // le
    # k = k - (le * cycle)
    # food_times = [X - cycle for X in food_times]
    print(food_times)
    while True:
        for i in range(le):
            print(food_times, k)
            if (food_times[i] > 0):
                food_times[i] -= 1
                k -= 1
                if (k == 0):
                    print(get_answer(i, le,food_times))
                    return get_answer(i, le,food_times)

    #
    # return answer


def get_answer(a, le,food_times):
    if()


# solution([3, 1, 2], 5)
# solution([4, 1, 10], 9)
# solution([10,2,15,9],21)
solution([1, 2, 3, 5], 10)
