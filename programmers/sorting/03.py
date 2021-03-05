# n개의 list안의 원소에서 h번 이상 사용된 원소가 h개 이상인데 나머지가 h번 이하인
# h의 최대값을 return

def solution(citations):
    answer = 0

    c = sorted(citations)

    print(c)
    for i in range(len(c)):
        # print('%d  %d element %d ' % (c[i], len(c[i:-1]+1), len(c[0:i])))
        if c[i] <= (len(c[i:-1])+1) and c[i] >= len(c[0:i]):
            answer = c[i]
    if c[0] >= len(c):
        answer = len(c)
    return answer


solution([3, 0, 6, 1, 5])
solution([22, 42])
