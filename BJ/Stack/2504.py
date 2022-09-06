


# a = list(sys.stdin.readline().strip())
# wrong = False
# stack = []
# new_stack =[]
# for i in a:
#     if(i =='('):
#         stack.append(i)
#     elif(i==')'):
#         if(stack[-1]=='('):
#             stack.pop()
#             stack.append(str(2))
#         else:
#             stack.append(i)
#     elif(i=='['):
#         stack.append(i)
    
#     elif(i==']'):
#         if(stack[-1]=='['):
#             stack.pop()
#             stack.append(str(3))
#         else:
#             stack.append(i)
#     # print(stack)

# for i in range(len(stack)-2):
 
#     if(stack[i]=='0'):
#         continue
        
#     if(stack[i]=='(' and stack[i+2]==')'):
#         if(stack[i+1].isdigit()):

#             new_stack.append(str(int(stack[i+1])*2))
#             stack[i],stack[i+1],stack[i+2]='0','0','0'
#         else:
#             print(0)
#             wrong =True
#             break
#     elif(stack[i]=='['and stack[i+2]==']'):
#         if(stack[i+1].isdigit()):
#             new_stack.append(str(int(stack[i+1])*3))
#             stack[i],stack[i+1],stack[i+2]='0','0','0'
#         else:
#             print(0)
#             wrong =True
#             break
#     else:
#         new_stack.append(stack[i])    
#     # print(new_stack)
# temp =0
# new_new_stack=[]
# if(wrong==False):

#     for i in new_stack:

#         if(i.isdigit()):
#             temp+=int(i)
#             # print(temp)
#         elif(i==')'):
#             if(new_new_stack[-1]=='('):
#                 new_new_stack.pop()
#                 new_new_stack.append(temp*2)
#                 temp =0
#             else:
#                 break
#         elif(i==']'):
#             if(new_new_stack[-1]=='['):
#                 new_new_stack.pop()
#                 new_new_stack.append(temp*3)
#                 temp=0
#             else:
#                 break
#         else:
#             new_new_stack.append(i)

#     print(new_new_stack[0]+temp)
#     # print(new_new_stack, temp)
import sys
a = sys.stdin.readline().strip()
stack=[]
top =-1
answer =0
temp =1

for i in range(len(a)):
    if a[i] =='(':
        stack.append(a[i])
        temp *=2
    elif a[i]=='[':
        stack.append(a[i])
        temp *=3
    elif a[i]==')':
        if not stack or stack[top] =='[':
            answer =0
            break
        if a[i-1] =='(':
            answer +=temp
        stack.pop()
        temp //=2
    elif a[i]==']':
        if not stack or stack[top] =="(":
            answer =0
            break
        if a[i-1] =='[':
            answer +=temp
        stack.pop()
        temp//=3
if stack:
    print(0)
else:
    print(answer)