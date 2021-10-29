import random
import time

## 전역변수 선언
m_t2 = 0
m_count = 0
h_count = 0

q_v1_count = 0
q_v1_t2 = 0


def insertion_sort(array):
    count = 0

    print("----insertion sort----")
    print("----정렬 전 배열----")
    print(array)

    n = len(array)
    start_time = time.time()
    for i in range(1, n):
        key = array[i]  # index 값을 key로 저장
        j = i - 1
        # 리스트의 j번째 값과 key를 계속 비교해 key가 들어갈 위치를 찾는 while문
        # while j >= 0 and array[j] > key:
        #     count += 1
        #     array[j + 1] = array[j]  # 값을 오른쪽으로 한칸 이동
        #     j -= 1  
        # array[j + 1] = key
        #
        # while j >= 0 and array[j] <= key:
        #     count += 1
        #     j -= 1
        while j >= 0:  # 모든 비교과정을 count 하기위한 조건식을 추가한 while문.
            if array[j] > key:
                count += 1

                j -= 1
            elif array[j] <= key:
                count += 1
                j -= 1
        array[j + 1] = array[j]  # 삽입할 공간이 생기게 값을 오른쪽으로 한칸 이동시킨다.
    end_time = time.time()

    print("----정렬 후 배열----")
    print(array)
    print("----배열 소요시간(초), 비교 횟수")
    print(end_time - start_time, count)

    return


def heap_sort(random_array):
    global h_count

    heap_size = len(random_array)
    t1 = time.time()
    # 리스트의 중앙에서부터 거꾸로 heapify를 해준다.
    for i in range(heap_size // 2 - 1, -1, -1):
        heapify(random_array, i, heap_size)
    # 루트값을 가장 끝 값으로 이동한 다음 heapify 실행
    for i in range(heap_size - 1, 0, -1):
        random_array[0], random_array[i] = random_array[i], random_array[0]

        heapify(random_array, 0, i)

        t2 = time.time()
    print("----정렬 후 배열----")
    print(random_array)
    print("----배열 소요시간(초), 비교 횟수")
    print(t2 - t1, h_count)


# 리스트가 힙인지 확인하고 재정렬
def heapify(unsorted, index, heap_size):
    global h_count

    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    # 자식 노드와 부모 노드와의 비교한뒤 자식노드가 부모노드보다 크면 인덱스를 스위치 해줍니다.
    if left < heap_size and unsorted[left] > unsorted[largest]:
        largest = left

    if right < heap_size and unsorted[right] > unsorted[largest]:
        largest = right
    # 부모 노드의 인덱스값이 변경되었으면 자식노드와 값을 스위치 해줍니다.
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        h_count += 1
        heapify(unsorted, largest, heap_size)  # heapify 재귀함수


def merge_sort(a):
    global m_count
    global m_t2

    m_t2 = 0
    if len(a) <= 1:  # 리스트의 길이가 1이될때 까지 분할 정복을 계속 진행한다.
        return a

    mid = len(a) // 2
    leftList = a[:mid]  # 중앙값을 기준으로 왼쪽과 오른쪽 리스트로 나눔
    rightList = a[mid:]
    leftList = merge_sort(leftList)  # 분할된 리스트를 계속 분할
    rightList = merge_sort(rightList)
    m_t2 = time.time()

    return merge(leftList, rightList)


def merge(left, right):  # 리스트를 병합하는 함수.
    global m_count
    global m_t2
    global m_t1
    result = []

    m_t1 = time.time()
    while len(left) > 0 or len(right) > 0:  # 왼쪽이나 오른쪽 모두 남아있을때.
        if len(left) > 0 and len(right) > 0:
            m_count += 1
            if left[0] <= right[0]:  # 왼쪽값과 오른쪽 값을 비교해서 작은값을 추가
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:  # 왼쪽만 남아있을때
            m_count += 1
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:  # 오른쪽만 남아있을때
            m_count += 1
            result.append(right[0])
            right = right[1:]

    m_t2 = time.time()  # 마지막 merge가 정렬이 끝난 시간

    return result


def quick_sort(arr, v):  # v는 version을 고르는 인자
    global pivot, q_v1_count, q_v1_t2

    if len(arr) <= 1:
        return arr
    if v == 1:  # version 1 : 배열의 첫번째 원소
        pivot = arr[0]
    elif v == 2:  # version 1 : 배열의 랜덤 값
        rand = (random.randrange(0, len(arr)))  # 배열의 길이의 범위내의 랜덤 숫자 추출
        pivot = arr[rand]

        # print("pivot: %d rand: %d" % (pivot, rand))
    elif v == 3:  # version 3 : 배열의 중앙 값
        pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []  # 피벗과 비교한 원소들을 넣을 배열
    for num in arr:
        q_v1_count += 1
        if num < pivot:  # 피벗보다 작은경우
            lesser_arr.append(num)

        elif num > pivot:  # 피벗보다 큰경우
            greater_arr.append(num)

        else:  # 피벗과 같은경우
            equal_arr.append(num)

    q_v1_t2 = time.time()
    # 재귀 함수로 피벗보다, 작은배열+ 같은 배열 + 큰 배열을 합친다.
    return quick_sort(lesser_arr, v) + equal_arr + quick_sort(greater_arr, v)


def make_random_array(n):  # n 크기의 랜덤 배열을 만드는 함수
    random_array = []
    while len(random_array) < n:  # n크기가 될때까지 배열에 원소를 추가
        temp = (random.randint(1, n))  # random 숫자를 1부터 n까지 계속 생성
        if temp not in random_array:  # 배열에 없으면 추가
            random_array.append(temp)
    return random_array


def main():
    global m_t2
    global m_count
    global h_count
    global q_v1_count
    global q_v1_t2
    while True:
        array = make_random_array(1000)
        print("숫자를 입력해서 정렬 알고리즘을 골라주세요!")
        print("1 - Insertion Sort")
        print("2 - Heap Sort")
        print("3 - Merge Sort")
        print("4 - Quick Sort v1")
        print("5 - Quick Sort v2")
        print("6 - Quick Sort v3")
        print("0 - 종료하기")
        num = int(input("숫자 입력 : "))

        if num == 1:
            insertion_sort(array)
        elif num == 2:
            heap_sort(array)
        elif num == 3:
            print(array)
            start_time = time.time()
            answer_array = merge_sort(array)
            print("----정렬 후 배열----")
            print(answer_array)
            print("----배열 소요시간(초), 비교 횟수")
            print(m_t2 - start_time, m_count)

        elif num == 4:
            q_v1_t1 = time.time()
            print(array)

            array = quick_sort(array, 1)
            print("----정렬 후 배열----")
            print(array)
            print("----배열 소요시간(초), 비교 횟수")
            print(q_v1_t2 - q_v1_t1, q_v1_count)

        elif num == 5:
            q_v1_t1 = time.time()
            print(array)
            array = quick_sort(array, 2)
            print("----정렬 후 배열----")
            print(array)
            print("----배열 소요시간(초), 비교 횟수")
            print(q_v1_t2 - q_v1_t1, q_v1_count)

        elif num == 6:
            q_v1_t1 = time.time()
            print(array)
            array = quick_sort(array, 3)
            print("----정렬 후 배열----")
            print(array)
            print("----배열 소요시간(초), 비교 횟수")
            print(q_v1_t2 - q_v1_t1, q_v1_count)

        elif num == 0:
            print("종료")
            break
        else:
            print("제대로 입력해주세요")
        print("다시 하기 - 1  종료 하기 - 0")
        num2 = int(input("숫자 입력 : "))
        if num2 == 1:
            h_count = 0
            m_count = 0
            q_v1_count = 0
            continue
        elif num2 == 0:
            break


main()
