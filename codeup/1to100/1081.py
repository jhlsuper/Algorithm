a = int(input(), 16)  # 뒤에 16을붙이면 16진수 input 16진수 int형으로 입력받음

for i in range(1, 16):
    print("%X*%X=%X" % (a, i, (a*i)))
