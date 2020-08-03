a = int(input())

result = []

result.insert(0,0)
result.insert(1,1)
result.insert(2,2)
result.insert(3,4)

for i in range(0, a):
    n = int(input())
    for j in range(4, n+1):
        result.insert(j,result[j-1]+ result[j-2]+result[j-3])
    print(result[n])