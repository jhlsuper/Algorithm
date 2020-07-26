a=int(input())
c=0
score=0
for i in range(0,a):
    c=0
    score=0
    b=list((input()))
    for i in range(len(b)):
        if b[i]=='O':
            c=c+1

            score=score+c
        elif b[i]=='X':

            c=0
    print(score)







