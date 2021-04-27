# def solution(prices):
#     answer = [0]*(len(prices))
#     real_answer = [0]*(len(prices))

#     for i in range(len(prices)-1):
#         print(i)
#         for j in range(i+1):
#             # print(i, j)

#             if answer[j] != -1:
#                 if prices[i] >= prices[j]:
#                     answer[j] += 1

#                 else:
#                     real_answer[j] = answer[j]
#                     answer[j] = -1

#             else:
#                 pass
#             # print(answer)
#     for z in range(len(prices)):
#         if answer[z] != -1:
#             real_answer[z] = answer[z]

#     # print(real_answer)
#     return real_answer

def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            if prices[i]<=prices[j]:
                answer[i]+= 1
            else:
                break

    return answer
solution([1, 2, 3, 2, 3])
