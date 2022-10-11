import sys 

N = int(sys.stdin.readline())
s = []
answer =0
step = 0
for i in range(N):
    a,b = map(int, sys.stdin.readline().split(" "))
    s.append([a,b])

for i in range(N):
    if(s[i][0]==1):
        answer +=s[i][1]
            