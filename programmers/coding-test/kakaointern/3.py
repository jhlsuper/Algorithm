def solution(n, k, cmd):
    answer = ''
    internlist = []
    for i in range(n):
        internlist.append(i)
    print(internlist)
    index = k
    stack = []

    for element in cmd:
        e = element.split(" ")
        if e[0] == 'U':
            index -= int(e[1])
            # print(index)

        elif e[0] == 'D':
            index += int(e[1])
        elif e[0] == 'C':

            stack.append(internlist[index])
            if index == len(internlist)-1:

                del internlist[index]
                index -= 1

            else:
                del internlist[index]

        elif e[0] == 'Z':

            value = stack.pop()
            if (value > len(internlist)-1):
                internlist.insert(len(internlist)-1, value)
            internlist.insert(value, value)
            if value < index:
                index += 1

        print(internlist)
        print(stack, index)
    for i in range(n):
        if i in internlist:
            answer += "O"
        else:
            answer += "X"

    print(answer)
    return answer


solution(8, 2, ["D 2", "C", "U 3", "C", "D 4",
                "C", "U 2", "Z", "Z", "U 1", "C"])
