from sys import stdin

a = list(stdin.readline().strip())
b = []

n = int(input())
for line in stdin:
    if line[0] =='L':
        if a: b.append(a.pop())
        else: continue
    elif line[0] =='D':
        if b: a.append(b.pop())
        else: continue
    elif line[0] =='B':
        if a: a.pop()
        else: continue
    elif line[0] =='P':
        a.append(line[2])

print(''.join(a+list(reversed(b))))