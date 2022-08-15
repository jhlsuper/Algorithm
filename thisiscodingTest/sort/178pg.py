from array import array
import sys
data = []
a = int(sys.stdin.readline())
for i in range(a):
    data.append(int(sys.stdin.readline()))

sorted_data = sorted(data, reverse=True)

for i in sorted_data:
    print(i, end = ' ')