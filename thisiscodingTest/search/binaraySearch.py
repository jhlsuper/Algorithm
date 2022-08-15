import sys
## 정렬되어있는 배열에서의 탐색 방법 
## 시간 복잡도 O(logN)

def binaray_search(array, target, start, end):
    if start > end:
        return None
    mid = (start +end) //2

    if array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return binaray_search(array, target, start, mid- 1)
    else:
        return binaray_search(array, target, mid +1, end)

n, target = list(map(int,(sys.stdin.readline().rstrip().split())))

array = list(map(int,(sys.stdin.readline().rstrip().split())))
print(array)
result = binaray_search(array, target, 0, n-1)
if(result ==None):
    print("찾으랴는 원소가 존재하지 않는다")
else:
    print(result+1 )