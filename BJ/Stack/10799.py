import sys 

a = list(sys.stdin.readline().strip())

stack =[]
answer =0
for i in range(len(a)):
    if(a[i] =='('):
        stack.append('(')
    else:
        if(a[i-1]=='('):
            stack.pop()
            answer+=len(stack)
        else:
            stack.pop()
            answer +=1
print(answer)


