a= int(input())
for i in range(1,a+1):
    b= list(input().split())

    largest=int(b[0])
    smallest=int(b[0])

    while i in b:
        if i>largest:
            largest=i

    while i in b:
        if i<smallest:
            smallest=i

        print(largest)


