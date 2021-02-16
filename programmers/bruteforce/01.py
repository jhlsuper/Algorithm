def solution(answers):
    answer = []
    i=0
    list1=[0,0,0]
    lost1 = [1,2,3,4,5]
    lost2 = [2,1,2,3,2,4,2,5]
    lost3 = [3,3,1,1,2,2,4,4,5,5]
    while i <len(answers):
        if lost1[i%5]== answers[i]:
            list1[0]+=1
        if lost2[i%8]==answers[i]:
            list1[1]+=1
        if lost3[i%10]==answers[i]:
            list1[2]+=1
    return list1
        
    # return answer
solution([1,2,3,4,5])