def solution(p):
    answer = ''
    stack = []
    # print(p)
# TODO 나중에 다시 풀어봅시다.. 20점
    for i in range(len(p)):

        if len(stack) == 0:
            stack.append([p[i], i])

        else:
            if p[i][0] == '(':

                stack.append([p[i], i])

            elif p[i][0] == ')':
                if stack[-1][0] == '(':
                    stack.pop()

                else:
                    stack.append([p[i], i])

    # print(stack)
    if len(stack) == 0:
        # print(p)
        answer =p
    else:

        for j in stack:
            # print(j[-1])
            p = list(p)

            if p[j[-1]] == '(':
                p[j[-1]] = ')'
            elif p[j[-1]] == ')':
                p[j[-1]] = '('
        # print(''.join(p))
        answer = ''.join(p)
        # print(p)
    # print(stack)
    print(answer)
    return answer


solution("(()())()")
solution(")(")
solution("()))((()")
