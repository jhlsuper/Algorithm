a,b,c = list(map(int,input().split()))

result = 0
if(c<=b):
    result = -1
else:
    result = a//(c-b)+1

print(result)
