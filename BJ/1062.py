def solution():
    n, k = map(int, input().split())
    list = []
    answer = 0
    five = ['a', 'n', 't', 'i', 'c']
    if k < 5:
        print(answer)
        return
    k -= 5
    for i in range(n):
        list.append(input()[4:-4])

    print(list)
    print(n, k)


solution()
