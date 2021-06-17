def exp(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    else:
        return a * exp(a, b - 1)


print(exp(10, 0))
