import heapq
import sys
heap =[]

N = int(sys.stdin.readline())

for i in range(N):
  number = int(sys.stdin.readline())
  if(number != 0):
    heapq.heappush(heap, (-number,number))
    
  else:
    if(len(heap)==0):
      print(0)
    else:
      
      print(heapq.heappop(heap)[1])
  # print(heap)
    