def Recursive_BinaryToDecimaL(n):
    if n == '0':
        return 0
    if n == '1':

        return 1
    else:
        # print(int(math.pow(2, len(n) - 1)) * int(n[0]), n[1:])
        return int(exp(2, len(n) - 1)) * int(n[0]) + (Recursive_BinaryToDecimaL(n[1:]))


def exp(a, b):
    result = 1
    if a == 0:
        result = 1
    else:
        for i in range(1, b + 1):
            result = result * a
    return result


def problem2():
    n = (input("2진수 입력: "))

    print("10진수 변환: %d" % (Recursive_BinaryToDecimaL(n)))


problem2()
