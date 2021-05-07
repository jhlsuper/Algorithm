def solution(numbers, hand):
    answer = ''
    L_position = 0
    R_position = 0
    left =[1,4,7]
    right = [3,6,9]
    middle = [2,5,8,0]

    L_diff = 0
    R_diff = 0
    for i in numbers:
        if i in left:
            answer+="L"
            L_position =left.index(i)+1 
        elif i in right:
            answer+="R"
            R_position =right.index(i)+1
        elif i in middle:
            L_diff = abs(L_position- middle.index(i))
            R_diff = abs(R_position - middle.index(i))
            if L_diff<R_diff:
                answer+="R"
            elif L_diff>R_diff:
                answer+="L"
            else :
                answer+=hand
        print(L_position,R_position)
            
        
    print(answer)
    return answer



solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right")
