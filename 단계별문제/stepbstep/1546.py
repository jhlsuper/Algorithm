a=int(input())
b=list(map(int, input().split()))
m_num=max(b)

for i in range(a):
    b[i]=b[i]/m_num*100
avg= sum(b)/a
print("%.2f" %avg)

