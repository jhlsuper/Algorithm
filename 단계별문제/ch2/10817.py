a,b,c=map(int,input().split())
result =a
if a>=b :
    if c<=b:
        result=b
    elif c>=b and c<=a:
        result=c
    else:
        result=a

elif a<=b:
    if c<=a:
        result=a
    elif c<=b and c>a:
        result=c
    else:
        result=b
print(result)

