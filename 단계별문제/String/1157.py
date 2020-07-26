a = list(input().upper())
c = [0]*26  ##알파벳 수만큼 리스트 생성

for i in a:
    c[ord(i)-65] += 1   #알파벳이 몇번 나오는지 하나씩 카운트
if c.count(max(c))>=2:
    print('?')
else:
    print(chr(c.index(max(c))+65))

#65~90 이 A~Z