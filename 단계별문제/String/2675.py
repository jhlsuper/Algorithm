a = int(input())

for i in range(0,a):
    result=''
    b = list(input().split())
    mul=int(b[0])
    c=list(b[1])

    for j in range(0,len(c)):
        result+=(mul*c[j])

    print(result)
