a = list(map(int, input().split()))

a = sorted(a)
first = 0
for i in range(a[1], a[0]*a[1]+1):
    if i % a[0] == 0 and i % a[1] == 0:
        first = i

        break

if a[2] > first:
    for i in range(a[2], first*a[2]+1):
        if i % a[2] == 0 and i % first == 0:
            first = i
            break
else:
    for i in range(first, first*a[2]+1):
        if i % a[2] == 0 and i % first == 0:
            first = i
            break
print(first)

# 3수의 최소 공배수를 구하는 방법
# 처음 작은 2개의 수의 최소공배수를 구하고 다음수와 최소공배수를 구한다.
