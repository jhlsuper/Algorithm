def insertion_sort(a):
    for end in range(1, len(a)):
        for i in range(end, 0, -1):
            if a[i - 1] > a[i]:
                a[i - 1], a[i] = a[i], a[i - 1]
        print(a)
    print(a)


insertion_sort([20,80,40,25,60,30])
