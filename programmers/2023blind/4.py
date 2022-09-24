


def solution(numbers):
    answer = []

    for i in numbers:
        no = True
        # print(format(i,'b'))
        temp =list(format(i,"b"))
        temp.reverse()
        # print(temp)
        
        for i in range(len(temp)):
            if(temp[i]=='0'):
                if((i+1)%2==0):
                    answer.append(0)
                    no = False
                    break
        if(no):
            answer.append(1)
    # print(answer)
    return answer
## 반대로 1 가능 111 가능 110 011 가능 

solution([63,111,95])