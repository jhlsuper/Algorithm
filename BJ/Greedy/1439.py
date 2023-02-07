import sys

# input2 = sys.stdin.readline
# sys.stdin.readline했더니 틀림
# a = input2()
count = 0

b = input()
# for i in a:
#     print(i)

for i in b:
    print(i)
# while (countA != len(a) and countB != len(a)):

for i in range(len(a) - 1):
    if a[i] != a[i + 1]:
        count += 1
print((count + 1) // 2)
