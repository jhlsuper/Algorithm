# def solution(number, k):
#     answer = ''
#     stack = []
#
#     for i in number:
#         while stack and stack[-1] < i and k > 0:
#             stack.pop()
#             k -= 1
#         stack.append(i)
#     while k > 0:
#         stack.pop()
#         k -= 1
#
#     answer = "".join(stack)
#     return answer
#
#
# solution("1924", 2)
# set1 ={1,3,5}
# set2 = {3.4,5}
#
# print(set1&set2)
# for i in range(5,0,-1):
#     print(i)

# greedy 알고리즘 문제를 해결할떄 그 순간순간 최적이라고 생각되는
# 결정을 하는것
