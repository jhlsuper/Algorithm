a,b=map(int,input().split())
L = list(map(int,input().split()))

for i in range(a):
    if L[i] <b:
        print(L[i],end=" ")