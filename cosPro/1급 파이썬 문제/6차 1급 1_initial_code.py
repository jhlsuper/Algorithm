#다음과 같이 import를 사용할 수 있습니다.
#import math
import numpy as np
def solution(n, garden):
    #여기에 코드를 작성해주세요.
    answer = 0
    v1 = np.array(garden)
    while(v1.sum() ==n*n): 
        for i in range(n):
            for j in range(n):
                if(garden[i][j]==1):
                    if(garden[i][j+1] != None):
                        garden[i][j+1] =1
                    if(garden[i][j-1]  != None):
                        garden[i][j-1] =1
                    if(garden[i+1][j]  != None):
                        garden[i+1][j] =1
                    if(garden[i-1][j]  != None):
                        garden[i-1][j]=1
        answer= answer+1
        
   
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n1 = 3
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(n1, garden1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 2
garden2 = [[1, 1], [1, 1]]
ret2 = solution(n2, garden2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")