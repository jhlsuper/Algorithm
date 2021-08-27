import statistics


def solution(a):
    answer = []

    for i in a:
        new_list = list(i)

        while len(new_list) > 2:
            new_list = cut_A(new_list)
            new_list = cut_B(new_list)
            # print(new_list)
        if(new_list==['a']):
            answer.append(True)
        else:
            answer.append(False)

    return answer


def cut_A(a):
    start, end = 0, len(a) - 1
    a_list = list(a)

    while a_list[start] == 'a':
        start += 1

    while a_list[end] == 'a':
        end -= 1
    return a_list[start:end + 1]


def cut_B(a):
    a_list = list(a)
    start, end = 0, len(a) - 1
    return a_list[start + 1:end]


# def add_A(a):


solution(["abab", "bbaa", "bababa", "bbbabababbbaa"])
