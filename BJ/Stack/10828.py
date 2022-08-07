import sys
from unittest import case
a = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(a)]
stack =[]
for i in data:
    temp = i.split(" ")
    if(temp[0])=='push':
        stack.append(temp[1])
    elif(temp[0])=='pop':
        if(len(stack)>0):
            print(stack.pop())
        else:
            print(-1)
    elif(temp[0])=='size':
        print(len(stack))
    elif(temp[0])=='empty':
        if( len(stack)>0):
            print(0)
        else:
            print(1)
      
    else :           # top      
        if(len(stack)>0):
            print(stack[-1])
        else:
            print(-1)

    


        
