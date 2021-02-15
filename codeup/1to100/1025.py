a = list(input())

for i in range(len(a)):
    print('[%d]' % (int(a[i])*(10 ** (len(a)-i-1))))
