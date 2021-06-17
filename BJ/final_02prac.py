def main():
    a = int(input("양의 정수를 입력하시오:"))
    for i in range(a):
        print(fib(i), end=' ')


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__=="__main__":
    main()