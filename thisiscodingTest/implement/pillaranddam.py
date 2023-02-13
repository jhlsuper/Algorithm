def solution(n, build_frame):
    answer = []
    for b in build_frame:
        x, y, what, op = b
        if op == 1:
            answer.append([x, y, what])
            if not check(answer):
                answer.remove([x, y, what])
        elif op == 0:
            answer.remove([x, y, what])
            if not check(answer):
                answer.append([x, y, what])
    answer.sort()
    # print(answer)
    return answer


def check(answer):
    for x, y, what in answer:
        if what == 0:
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        elif what == 1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True


solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
             [3, 2, 1, 1]])
