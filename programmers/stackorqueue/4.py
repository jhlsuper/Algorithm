def solution(priorities, location):
    answer = 0
    stack = []
    index =0
    t =0
    answer_list=[]
    for i in priorities:
        stack.append([i,index])
        index+=1
    print(stack)
    while stack:
        for i in range(len(stack)):
            temp = stack.pop(0)
            
            for j in stack:
                
                if temp[0]<j[0] : ##우선순위가 낮은경우
                    t+=1        
                else:   
                    continue
                    # print(answer_list)
            if t>0:
                stack.append(temp)
            else:
                answer_list.append(temp[1])
            t =0
            
    # print(answer_list[location][0])
    answer = answer_list.index(location)+1
    # print(answer)
    return answer

    
        
    # solution([2, 1, 3, 2], 2)
solution([1, 1, 9, 1, 1, 1]	,0)