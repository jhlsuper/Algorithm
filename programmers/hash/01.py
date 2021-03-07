def solution(participant, completion):
    hash ={}

    for i in participant:
        if i in hash:
            hash[i]+=1
        else:
            hash[i]=1
    for i in completion:
        if hash[i] ==1:
            del hash[i]
        else:
            hash[i] -=1
    answer = list(hash.keys())[0]
    return answer


##participant 리스트에는 마라톤 경기에 참여한 선수숫자
##completion 은 마무리한 사람의 숫자 
##결과로는 마무리하지 못한 선수를 구하라!

##list.remove(찾을아이템)