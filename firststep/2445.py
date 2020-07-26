a = int(input())

for i in range(1,a):
    print('*'*i + ' '*((a-i)*2) + '*'*i)

print('*'*(2*a))

for j in range(1,a):
    print('*' * (a-j) + ' '*j*2 + '*' * (a-j))
