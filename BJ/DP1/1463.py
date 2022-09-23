import sys

n = int(sys.stdin.readline())
answer = 0

dp=[0]*1000001

for i in range(2, n+1):
    dp[i] = dp[i-1]+1
    if(i%3==0):
        dp[i] =min(dp[i],dp[i//3]+1)
    elif(i%2==0):
<<<<<<< HEAD
        dp.append(dp[i//2]+1)
    else:
        dp.append(dp[i]+1)
        
    
=======
        dp[i]=min(dp[i],dp[i//2]+1)
print(dp[n])
        
>>>>>>> 3448ae5eff8dc71d49b388f127bb5a895805eaad
