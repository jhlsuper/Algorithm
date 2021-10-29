import random
import time

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

    start_time = time.time()
    n = len(array)
    for i in range(1, n):
        key = array[i]  # index 값을 key로 저장
        j = i - 1
        count += 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]  # 값을 오른쪽으로 한칸 이동
            j -= 1
        array[j + 1] = key
    # for end in range(1, len(array)):
    #
    #     for i in range(end, 0, -1):
    #         count += 1
    #         if array[i - 1] > array[i]:
    #             array[i - 1], array[i] = array[i], array[i - 1]
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

    for i in range(heap_size // 2 - 1, -1, -1):
        heapify(random_array, i, heap_size)

    for i in range(heap_size - 1, 0, -1):
        random_array[0], random_array[i] = random_array[i], random_array[0]
        heapify(random_array, 0, i)

        t2 = time.time()

    print(random_array)
    print(t2 - t1)
    print(h_count)


def heapify(unsorted, index, heap_size):
    global h_count
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < heap_size and unsorted[left] > unsorted[largest]:
        largest = left
        h_count += 1
    if right < heap_size and unsorted[right] > unsorted[largest]:
        largest = right
        h_count += 1
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        h_count += 1
        heapify(unsorted, largest, heap_size)


def merge_sort(a):
    global m_count
    global m_t2
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    leftList = a[:mid]
    rightList = a[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    m_t2 = time.time()
    # print(m_t2)

    return merge(leftList, rightList)


def merge(left, right):
    global m_count
    global m_t2
    global m_t1
    result = []
    m_t1 = time.time()
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            m_count += 1
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            m_count += 1
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            m_count += 1
            result.append(right[0])
            right = right[1:]
        # print(result)
    # print(result)

    m_t2 = time.time()
    print(m_t2)
    return result


# def quick_sort_v1(array, s, e, v):
#     global q_v1_count, pivot
#     global q_v1_t2
#     if s >= e:
#         return
#     if v == 1:
#         pivot = s # 첫번째 원소를 pivot으로
#         print(pivot)
#     elif v == 2:
#         pivot = (random.randint(s, e))
#
#         print("pivot: %d"%pivot)
#     elif v == 3:
#         pivot = int((e - s) / 2) + 1
#
#         print(pivot)
#     left = s + 1
#     right = e
#
#     while left <= right:
#
#         while left <= e and array[left] <= array[pivot]:
#             left += 1
#             q_v1_count += 1
#         while right > s and array[right] >= array[pivot]:
#             right -= 1
#             q_v1_count += 1
#         if left > right:
#             # q_v1_count +=1
#             array[right], array[pivot] = array[pivot], array[right]
#         else:
#
#             array[left], array[right] = array[right], array[pivot]
#     q_v1_t2 = time.time()
#     # print(q_v1_t2)
#     quick_sort_v1(array, s, right - 1, v)
#     quick_sort_v1(array, right + 1, e, v)
def quick_sort(arr, v):
    global pivot, q_v1_count, q_v1_t2

    if len(arr) <= 1:
        return arr
    if v == 1:

        pivot = arr[0]
    elif v == 2:
        rand = (random.randrange(0, len(arr)))
        pivot = arr[rand]

        print("pivot: %d rand: %d" % (pivot, rand))
    elif v == 3:
        pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        q_v1_count += 1
        if num < pivot:
            lesser_arr.append(num)
            # q_v1_count += 1
        elif num > pivot:
            greater_arr.append(num)
            # q_v1_count += 1
        else:
            equal_arr.append(num)
            # q_v1_count += 1
    q_v1_t2 = time.time()

    return quick_sort(lesser_arr, v) + equal_arr + quick_sort(greater_arr, v)


def make_random_array(n):
    random_array = []
    while len(random_array) < n:
        temp = (random.randint(1, n))
        if temp not in random_array:
            random_array.append(temp)
    return random_array


def main():
    global m_t2
    global m_count

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
            print(answer_array)
            print(m_count)
            print(m_t2 - start_time)

        elif num == 4:
            q_v1_t1 = time.time()
            # print(array)
            # quick_sort_v1(array, 0, len(array) - 1, 1)
            array = quick_sort(array, 1)
            print(array)
            print(q_v1_t2 - q_v1_t1)
            print(q_v1_count)
        elif num == 5:
            q_v1_t1 = time.time()
            array = quick_sort(array, 2)
            # quick_sort_v1(array, 0, len(array) - 1, 2)
            print(array)
            print(q_v1_t2 - q_v1_t1)
            print(q_v1_count)
        elif num == 6:
            q_v1_t1 = time.time()
            array = quick_sort(array, 3)
            # quick_sort_v1(array, 0, len(array) - 1, 3)
            print(array)
            print(q_v1_t2 - q_v1_t1)
            print(q_v1_count)
        elif num == 0:
            print("종료")
            break
        else:
            print("제대로 입력해주세요")
        print("다시 하기 - 1  종료 하기 - 0")
        num2 = int(input("숫자 입력 : "))
        if num2 == 1:
            continue
        elif num2 == 0:
            break


main()
