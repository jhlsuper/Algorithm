def IS_PNum(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def make_primeList(z):
    primeList = []
    for i in range(z + 1):
        if (IS_PNum(i)):
            primeList.append(i)
    return primeList


def problem3():
    a = int(input("a 입력: "))
    b = int(input("b 입력: "))
    primeList = make_primeList(a)
    print("%d보다 작은 %d의 가장 큰 소수: " % (a, b), end="")
    for i in range(b-1):
        print(primeList.pop(), end=", ")
    print(primeList.pop())

problem3()
