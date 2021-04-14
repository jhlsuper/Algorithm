from typing import Dict


def solution(clothes):
    dictionary = {}
    gop = 1
    
    for i in clothes:
        if i[-1] in dictionary:
            dictionary[i[-1]]+=1
        else:
            dictionary[i[-1]]=1
    # print(dictionary)
    for val in dictionary.values():
        gop=gop*val
    
    if len(dictionary)==1:
        return(gop)
    else:
        return(len(clothes)+gop)

    return gop
             
    
    # answer = 0
    # return answer


solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], 
["green_turban", "headgear"]])