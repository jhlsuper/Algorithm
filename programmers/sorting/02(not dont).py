def solution(numbers):
    answer = ''
    myList = sorted(numbers, key=str)

    for i in range(len(numbers)-1,-1,-1):
        answer= answer+(str(myList[i]))


    print(answer)

solution([6, 10, 2])
