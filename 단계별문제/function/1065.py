a=int(input())
h=0

for i in range(1,a+1):
    if i<=99:
        h +=1

    else:
        nums=list(map(int,str(i)))
        if nums[0]-nums[1]==nums[1]-nums[2]:
            h+=1
print(h)





