import string

tmp = string.digits + string.ascii_lowercase


def solution(n, t, m, p):
    ## n: 진법 t: 미리 구할 숫자의 갯수 , m 게임에 참가하는 인원, p 튜브의 순서
    number_list = []
    answer = ''
    temp = []
    last_num = (t - 1) * m + p
    for i in range(last_num):

        if len(temp) <= last_num:
            for j in range(len(list(convert(i, n)))):
                temp.append(list(convert(i, n))[j])
    for i in range(p - 1, last_num, m):
        answer += temp[i]
    # print(temp)
    # print(answer)
    return answer.upper()


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


solution(2, 4, 2, 1)
# solution(16, 16, 2, 1)
