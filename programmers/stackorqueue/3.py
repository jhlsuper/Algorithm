def solution(progresses, speeds):
    answer =[]    
       
    index =0
    length = 0
    # progresses.pop(0)
    # print(progresses)
    while progresses:
        
        # print(progresses)
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]
        print(progresses)
        if len(progresses)==1:
            progresses.pop()
            answer.append(1)
            break
        while progresses[0]>=100:
            
            if len(progresses)==1:
                length+=1
                progresses.pop(0)
                answer.append(length)
                length=0
                break
            
            progresses.pop(0)
            speeds.pop(0)
            length +=1
            index +=1
            
        if (length > 0):
            answer.append(length)
            length =0
            index =0
        print(answer)
            
            
    print(answer)
    return answer


solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])