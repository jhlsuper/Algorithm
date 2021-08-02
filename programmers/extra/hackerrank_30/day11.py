def solution():
    arr = []
    temp = 0
    biggest =-9999   ##음수값을 생각해야된다.
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(arr)

    for i in range(4):
        for j in range(4):
            temp += arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + \
                    arr[i + 2][j + 2]

            if temp > biggest:
                biggest = temp
            temp = 0
    print(biggest)


solution()
