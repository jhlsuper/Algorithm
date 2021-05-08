def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        
        for j in range(i+1,len(numbers)):
            # print('i: {0}, j: {1}'.format(i,j))
            if (numbers[i]+numbers[j]) not in answer:
                answer.append(numbers[i]+numbers[j])

    answer.sort()
    # print(answer)
    return answer

solution([2,1,3,4,1])