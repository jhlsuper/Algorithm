import sys
a = int(input())
matrix = [[0 for col in range(19)]for row in range(19)]
# columm 열 row 행    세로 가로
z = 0
while z < a:
    b, c = map(int, input().split())
    matrix[b-1][c-1] += 1
    z = z+1
for i in matrix:
    for j in i:
        print(j, end=" ")
    print()
