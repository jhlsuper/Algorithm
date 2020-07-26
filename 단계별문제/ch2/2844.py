H,M =map(int,input().split())

if M<45:
    if H==0:
        H=23
        M = 60 - (45 - M)
    else:
        H=H-1
        M=60-(45-M)

else:
    M=M-45

print(H, M)