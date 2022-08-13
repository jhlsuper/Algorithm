import sys

a,b = map(int,sys.stdin.readline().split())

arr= []
answer = []
num = 0
for i in range(1,a+1):
    arr.append(i)

for i in range(b):
    num += b-1
    if num>= len(arr):
        num = num%len(arr)
    
    answer.append(str(arr.pop(num)))
print("<",", ".join(answer)[:],">", sep='')
