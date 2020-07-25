S = list(input())

b = []
for i in range(len(S)):
    #print("".join(S[i:]))
    t = ("".join(S[i:]))
    b.append(t)
b = sorted(b)
for j in range(len(b)):
    print(b[j])



