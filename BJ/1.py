def exp(a, b):
    if b == 0:
        return 1
    else:
        return a * exp(a, b - 1)


def problem1():
    a = int(input("밑수 입력 : "))
    b = int(input("지수 입력 : "))
    print(a, "의", b, "승은", exp(a, b))


problem1()
