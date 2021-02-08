def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        newarray = sorted(array[commands[i][0]-1:commands[i][1]])
        print(newarray)
        answer.append(newarray[commands[i][2]-1])
    return answer

    '''더욱 쉬운 정답
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
    '''
