a,b = map(list,input().split())
c = []
d = []

for i in range(0,3):
    c.append((a[2-i]))
    d.append((b[2-i]))
    e="".join(c)
    f="".join(d)
if e>f:
    print(e)
else:
    print(f)

#리스트의 join 활용법