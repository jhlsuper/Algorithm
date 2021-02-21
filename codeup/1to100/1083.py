a, b, c = map(int, input().split())
output = 0
for i in range(a):
    for j in range(b):
        for h in range(c):
            print("%d %d %d" % (i, j, h))
            output += 1

print(output)
