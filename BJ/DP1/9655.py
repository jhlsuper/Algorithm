import sys 

N = int(sys.stdin.readline())

DP = [-1]*1001
DP[1] = 1
DP[2] = 0
DP[3] =1

for i in range(4, N+1):
    if(DP[i-1] or DP[i-3]):
        DP[i] =0
    else:
        DP[i]=1
if(DP[N] ==0):
    print("CY")
else:
    print("SK")