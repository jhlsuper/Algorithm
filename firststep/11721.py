a = str(input())

while len(a)>10:
    print(a[0:10])
    a=a[10:]
if len(a)<=10:
    print(a)