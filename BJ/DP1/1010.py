import sys
import math

n = int(sys.stdin.readline())

for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    answer = math.factorial(b) //(math.factorial(a)*math.factorial(b-a))
    print(answer)