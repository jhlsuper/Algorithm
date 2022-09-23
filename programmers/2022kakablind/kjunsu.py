import string
import math
temp = string.digits


def convert(num,base):


    q,r = divmod(num,base)
    if q ==0:
        return temp[r]
    else:
        return convert(q,base)+temp[r]

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i ==0:
            return False
    return True

def solution(n, k):
    answer = 0
    if k ==10:
        a = str(n)
    else:

        a = convert(n,k)
    # print(a)
    
    split = a.split("0")
    
    for i in (split):
        if(i):
            # print(i)
            if is_prime_number(int(i)) and int(i) !=1:
                answer +=1
    # print(answer)
    return answer

solution(110011,10)