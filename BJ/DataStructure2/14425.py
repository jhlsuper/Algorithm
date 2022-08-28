import sys

N,M = map(int, sys.stdin.readline().split())

whole_list = [sys.stdin.readline().strip() for i in range(N)]

part_list = [sys.stdin.readline().strip() for i in range(M)]

whole_set = set(whole_list)
part_set = set(part_list)
answer =0
# print(len(whole_set & part_set))
for i in part_list:
  if(i in whole_set):
    answer = answer+1

print(answer)