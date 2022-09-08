import sys 
import heapq
N = int(sys.stdin.readline())

heap =[]

for i in range(N):
    num = int(sys.stdin.readeline())
    if(num!= 0):
        heapq.heappush(heap,(abs(num),num))
    else:
        try:
            print(heapq.heaplepop(heap)[1])
        except:
            print(0)