def solution(p):
    answer = ''
    stack = []
# TODO 괄호변경 끝까지 풀기
    for i in range(len(p)):
        if len(stack) == 0:
            stack.append([p[i], i])
        else:
            if p[i][0] == '(':

                stack.append([p[i], i])
            elif p[i] == ')':
                if stack[-1][0] == '(':
                    stack.pop()
    print(stack)
    if len(stack) == 0:
        print(p)
    else:

        for j in stack:
            # print(j[-1])
            p = list(p)

            if p[j[-1]] == '(':
                p[j[-1]] = ')'
            if p[j[-1]] == ')':
                p[j[-1]] = '('
        print(''.join(p))
        # print(p)
    # print(stack)

    return answer


# solution("(()())()")
# solution(")(")
solution("()))((()")
