a=list(input())
b=list()

for i in a:
    b.append(ord(i))

for j in range(97,123):
    if j in b:
        print(b.index(j))
    elif j not in b:
        print('-1')


##for i in range(0,a):
