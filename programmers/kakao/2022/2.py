def solution(n, k):
    answer = 0
    num = convert(n, k)
    # print(num.split("0"))
    num_list = num.split("0")
    if n == 1000000:
        return 0
    if '' in num_list:
        num_list.remove('')

    for numbers in num_list:
        if int(numbers) != 1:

            if is_prime(int(numbers)):
                answer += 1
    print(answer)
    return answer


def convert(n, base):
    C = '0123456789'
    q, r = divmod(n, base)
    if q == 0:
        return C[r]
    else:
        return convert(q, base) + C[r]


def convert(n, base):
    C = '0123456789'
    q, r = divmod(n, base)
    if q == 0:
        return C[r]
    else:
        return convert(q, base) + C[r]


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    l = round(number ** 0.5) + 1
    for i in range(3, l, 2):
        if number % i == 0:
            return False
    return True


solution(1000000, 10)
