import sys

a = int(sys.stdin.readline())

for i in range(a):
    answer =0
    N, wanna_know = map(int, sys.stdin.readline().split(" "))
    # priority =[]
    # for i in range(N):
    li =(sys.stdin.readline().strip().split(' '))
    
    for i in (li):
        if(i>=li[wanna_know]):
            answer+=1
    