a, b = map(int, input().split())
count = 0

while b > a:

    if str(b)[-1] == str(1):

        b = int(str(b)[0:-1])

        count += 1
    else:
        if b % 2 == 0:

            b = int(b / 2)

            count += 1
        else:
            break
if b == a:

    print(count + 1)
else:
    print(-1)
