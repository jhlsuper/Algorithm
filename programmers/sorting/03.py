def solution(citations):
    answer = 0

    c = sorted(citations)

    # print(c)
    for i in range(len(c)):
        # print('%d  %d element %d ' % (c[i], len(c[i:-1]+1), len(c[0:i])))
        if c[i] <= (len(c[i:-1])+1) and c[i] >= len(c[0:i]):
            answer = c[i]
    if c[0] >= len(c):
        answer = len(c)
    print(answer)
    return answer
solution([20,18,19,1])    
'''위의 방법으로 풀면 
[20,18,19,1] ==>  3 
이런 문제를 풀지 못한다.

citations 값~0까지 모든값을 탐색한다. 
def solution(citations):
    for z in revsered(range(max(citations)+1)):
        new_list=[i for i in citations if i>=z]
        if (z <=len(new_list)):
            return z
    
'''