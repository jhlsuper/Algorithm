def fib_tab(n):
    # 코드를 작성하세요.
    a = []
    if n < 3:
        return 1
    else:
        for i in range(1, n+1):
            if i < 3:
                a.append(1)

            else:
                adder = (a[i-2] + a[i-3])
                a.append(adder)
    return a[n-1]


# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))
