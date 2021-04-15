def solution(s):
    answer = 0

    stack = []

    for i in s:
        stack.append(i)
    if checkright(stack) == True:
        answer += 1
        # print(stack)
    for i in range(len(s)-1):
        # stack.pop()
        stack.append(stack[0])
        del stack[0]
        # print(stack)
        if checkright(stack) == True:
            answer += 1
            # print(True)

            # print(answer)
    return answer


def checkright(list):
    newstack = []
    answer = True
    dictionary = {')': '(', '}': '{', ']': '['}
    for z in list:
        if z == '(' or z == '{' or z == '[':
            newstack.append(z)
        else:
            if len(newstack) == 0 or newstack.pop() != dictionary[z]:
                answer = False
                break
    if len(newstack) != 0:
        answer = False
    return answer


solution("[](){}")
