import sys

n = int(sys.stdin.readline())

DP =[0 for i in range(n+2)]
DP[1] =1

if(n ==0):
    print(DP[0])
elif(n==1):
    print(DP[1])
else:
    for i in range(2,n+1):
        DP[i] = DP[i-1]+DP[i-2]

    print(DP[i])


def fibo(i):
    if(i==0):
        return 0
    elif(i==1):
        return 1
    else:
        return fibo(i-1)+fibo(i-2)

for i in range(6):
    print(fibo(i))