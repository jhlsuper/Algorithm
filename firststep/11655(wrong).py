a = list(input())
i=0
j=0
for i in range(len(a)):
    if ord(a[i])>64 and ord(a[i]) < 78:
        #print(chr(ord(a[i])+13))
        a[i] = chr(ord(a[i])+13)
    elif ord(a[i])>77 and ord(a[i])< 91:
        a[i] = chr(ord(a[i])-13)
    elif ord(a[i])>96 and ord(a[i])< 109:
        a[i] = chr(ord(a[i])+13)
    elif ord(a[i])>109 and ord(a[i])< 123:
        a[i] = chr(ord(a[i])-13)
        
for j in range(len(a)):
    print(a[j],end='')

