a=int(input())
avg=0
d=0
result=0
for i in range(0,a):
    avg=0
    d=0
    result=0
    c=list(map(int,input().split()))
    b=c.pop(0)
    for i in range(0,b):
        score_sum=(sum(c))

        avg=score_sum/b
    for i in range(0,b):
        if c[i]>avg:
            d=d+1
            result=d/len(c)*100
    print("%.3f%%" %(result))
    #print(round(result,3))

