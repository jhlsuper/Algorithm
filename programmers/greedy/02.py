def solution(name):
    answer = 0
    length = len(name)
    A_list = ['A']*length
    name_list = list(name)
    
    while A_list !=name_list:
        for i in range(length):
            if 65<ord(name_list[i])<78 :
                A_list[i]=name_list[i]
                answer+= ord(name_list[i])-65
                    
            elif 78<=ord(name_list[i])<91:
                A_list[i]= name_list[i]
                answer+=91-ord(name[i])
            answer+=1
    print(A_list)
    print(answer)
    
    
    
    return answer-1

solution("JEROEN")


##파이썬 문자열 아스키 코드로 바꾸기 
## ord("a")  -> 97
## 아스키 코드를 문자열로 바꾸기 
## chr(65) -> 65

## 65 -> A   90 -> Z  97 -> a  122-> z 