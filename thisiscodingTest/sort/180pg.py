import sys

a = int(sys.stdin.readline())
data = []
for i in range(a):
    temp = sys.stdin.readline().split()
    data.append((temp[0],temp[1]))


array = sorted(data, key = lambda a: a[1])

for i in array: 
    print(i[0], end = ' ')