n = int(input())
dict = {}
for i in range(0,n):
    a = input().split(" ")
    dict[a[0]] = a[1]

for j in range(0,n):
    try:
        b = input()
        if b in dict:
            print(b + "=" + dict[b])
        else:
            print("Not found")
    except:
        break