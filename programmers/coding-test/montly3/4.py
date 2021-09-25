def solution(a, s):
    index = 0

    c = []
    temp =[]
    len_b = len(s)
    for z in range(0, len_b):
        i = 1
        temp = a[index:index + s[z]]
        index += s[i]
        print(temp,1)
        while i != len(temp):
            print(i)
            if temp[i] == temp[i - 1]:

                temp[i - 1] = temp[i] + temp[i - 1]
                del temp[i]
                c.append(i)

            else:
                i += 1
            print(temp)


    print(c)

    answer = []
    return answer


solution([1, 1, 1, 1, 1, 1, 2, 5, 8, 2, 1, 1, 4, 8, 8, 8, 12, 6, 6], [4, 3, 1, 5, 6])
