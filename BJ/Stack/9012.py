import sys
def solove(input):
    stack =[]
    for i in input :
        if(i=='('):
            stack.append('(')
        else:
            if(len(stack)>0):
                
                if("(" in stack):
                    stack.pop()
                            
            else:
                stack.append(')')
    # print(stack)
    if(len(stack)==0):
        print("YES")
    else:
        print("NO")
            

a = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(a)]
for i in data:
    solove(i)     
