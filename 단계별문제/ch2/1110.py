
a=int(input())
count=0

if a<10:
    a='0'+str(a)

else:
    a=a
new_num=a
while True:

    new_sum = int(list(str(new_num))[0]) + int(list(str(new_num))[1])
    #print("sum:",new_sum)
    new_num=int(list(str(new_num))[1]+list(str(new_sum))[-1])
    #print("num:",new_num)
    if new_num<10:
        new_num='0'+str(a)
    count+=1

    if a==new_num:
        print(count)
        break










#sum([int(i) for i in str(a)])
#sum(map(int,str(a)))