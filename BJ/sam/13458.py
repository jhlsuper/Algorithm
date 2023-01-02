import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split(' '))) 
B,C = map(int, sys.stdin.readline().split(' '))

print(N,A,B,C)

for i in range(A):
    if (B>=C):
        