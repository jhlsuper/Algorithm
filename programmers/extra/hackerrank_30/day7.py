import math
import os
import random
import re
import sys

n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

for i in range(len(arr)):
    print(arr[len(arr) - 1 - i], end='')
