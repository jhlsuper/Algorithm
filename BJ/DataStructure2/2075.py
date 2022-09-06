import sys 
import heapq
heap =[]
n = int(sys.stdin.readline())

for _ in range(n):
    numbers = map(int, sys.stdin.readline().split())

    for i in numbers:
        if(len(heap)<n):
            heapq.heappush(heap,i)
        else:
            if(heap[0]<i):
                # print(heap,i)
                heapq.heappop(heap)
                heapq.heappush(heap,i)

print(heap[0])