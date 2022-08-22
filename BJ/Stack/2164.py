import sys
from collections import deque

a = int(sys.stdin.readline())
deque = deque([i for i in range(1,a+1)])

while(len(deque)>1):
    deque.popleft()
    temp = deque.popleft()
    deque.append(temp)

print(deque[0])