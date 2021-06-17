def sum1(a, b):
    a_split = a.split("+")
    b_split = b.split("+")
    a_1 = float(a_split[0])
    a_2 = float(a_split[1][:-1])
    b_1 = float(b_split[0])
    b_2 = float(b_split[1][:-1])
    print("[합의결과] %.2f+%.2fi" % ((a_1 + b_1), (a_2 + b_2)))


def mul(a, b):
    a_split = a.split("+")
    b_split = b.split("+")
    a_1 = float(a_split[0])
    a_2 = float(a_split[1][:-1])
    b_1 = float(b_split[0])
    b_2 = float(b_split[1][:-1])

    print("[곱의결과] %.2f+%.2fi" % ((a_1 * b_1) - (a_2 * b_2), (a_1 * b_2) + (a_2 * b_1)))


def answer():
    a = input("복소수 1입력:")
    b = input("복소수 2 입력:")
    sum1(a, b)
    mul(a, b)


answer()
