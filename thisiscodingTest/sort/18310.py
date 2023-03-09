n = int(input())
li = []
li = list(map(int, input().rstrip().split()))
li.sort()
print(li[(n-1)//2])