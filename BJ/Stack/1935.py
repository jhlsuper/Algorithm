import sys


def calc(a,b,sign):
  if(sign =="*"):
    return a*b
  elif(sign=="+"):
    return a+b
  elif(sign=='/'):
    return b/a
  elif(sign=='-'):
    return b-a
    

N = int(sys.stdin.readline())
line = sys.stdin.readline().strip()
stack=[]
new_stack=[]
number_stack = []
for i in range(N):
  temp = int(sys.stdin.readline())
  number_stack.append(temp)

# print(line, number_stack)

for a in line:
    if(a.isalpha()):

        temp = number_stack[ord(a)-65]
        new_stack.append(temp)
    else:
        new_stack.append(a)
# print(new_stack)
for a in new_stack:
   
    if(type(a)==int):
        stack.append(a)
    else:
        temp_a = stack.pop()
        temp_b = stack.pop()
        result= calc(temp_a,temp_b, a)
        stack.append(result)

print(format(stack[0],".2f"))

