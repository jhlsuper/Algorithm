a = int(input())

for i in range(1,a+1):
    print(" "*(a-i)+'*'*i)

for j in range(1,a):
    print(" "*j+'*'*(a-j))
