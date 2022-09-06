import sys
input = sys.stdin.readline
dict ={}
count =0
while True:
    a= input().rstrip()
    if not a:
        break
    if a in dict:
        dict[a] +=1
        count+=1
    else:
        dict[a] =1
        count+=1

tree_list = list(dict.keys())
# print(tree_list)
tree_list.sort()

for a in tree_list:
    print('%s %.4f' %(a, dict[a]/count*100))