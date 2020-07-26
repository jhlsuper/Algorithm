x, y =map(int,input().split())

day = 0
dayList = [31,28,31,30,31,30,31,31,30,31,30,31]
weekList = ["SUN","MON","TUE","WED","THU","FRI","SAT"]

for i in range(x-1):
    day = day+dayList[i]
day = (day+y)%7

print(weekList[day])


