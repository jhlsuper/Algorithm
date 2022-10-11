import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split(' '))) 
B,C = map(int, sys.stdin.readline().split(' '))
answer =[]
# print(N,A,B,C)

for i in A:
    count =0
    
    
    i=i-B;
    count+=1
    if(i>0):
        count+= i//C
        if(i%C)!=0:
            count +=1
    
    answer.append(count)

print(sum(answer))

        
        
    