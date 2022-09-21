import sys

n = int(sys.stdin.readline())
answer = 0

dp=[0,0,1.1]

for i in range(4, n+1):
    print(i)
    if(i%3==0):
        dp.append(dp[i//3]+1)
    elif(i%2==0):
        dp.append(dp[i//2]+1)
    else:
        dp.append(dp[i]+1)
        
        