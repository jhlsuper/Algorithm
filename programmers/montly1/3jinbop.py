def solution(n):
    answer = 0
    a = n
    list =[]
    while a >0:
        div = a//3
        mod = a%3
        a = div
        list.append(mod)
    
    i =0
    for i in range(len(list)):
        # print(list[i])
        
        answer+= list[len(list)-1-i]*(3^i)
    print(answer)
    return answer


solution(45)