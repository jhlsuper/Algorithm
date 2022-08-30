import sys
from collections import deque

n = int(sys.stdin.readline())

deq = deque(enumerate(map(int, sys.stdin.readline().split()),start=1))

# print(deq)

for i in range(n):
    temp = deq.popleft()
    print(temp[0], end=' ')
    if(temp[1]>0):
        deq.rotate(-(temp[1]-1))
    else:
        deq.rotate(-temp[1])


# deque (덱)

# double ended queue 

# deque.append(a)  오른쪽 끝에 추가 
# deque.appendleft(a)  왼쪽 끝에 추가 

# deque.extent(iterable) iterable argument(list, str, tuple)는 arguments의 각 요소를 하나씩 
# 변환 가능한 object를 의미  (나눠서 )
