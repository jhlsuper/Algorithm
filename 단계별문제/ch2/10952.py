a=b=3
while a!=0and b!=0:
    a, b = map(int, input().split())
    if a==0 and b==0 :
        break
    print('%d'%(a+b))



