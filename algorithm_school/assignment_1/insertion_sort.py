import random
import time

global m_count
m_count: int = 0


def insertion_sort(array):
    count = 0

    print("----insertion sort----")
    print("----정렬 전 배열----")
    print(array)

    start_time = time.time()
    for end in range(1, len(array)):
        for i in range(end, 0, -1):
            count += 1
            if array[i - 1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]
    end_time = time.time()
    print("----정렬 후 배열----")
    print(array)
    print("----배열 소요시간(초), 비교 횟수")
    print(end_time - start_time, count)

    return


def heap_sort(random_array):
    count = 0
    heap_size = len(random_array)
    t1 = time.time()
    print("t1--")
    print(t1)
    for i in range(heap_size // 2 - 1, -1, -1):
        heapify(random_array, i, heap_size)
        count += 1
    for i in range(heap_size - 1, 0, -1):
        random_array[0], random_array[i] = random_array[i], random_array[0]
        heapify(random_array, 0, i)
        count += 1
        t2 = time.time()

    print(random_array)
    print(t2 - t1)


def heapify(unsorted, index, heap_size):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < heap_size and unsorted[left] > unsorted[largest]:
        largest = left
    if right < heap_size and unsorted[right] > unsorted[largest]:
        largest = right
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)


def merge_sort(a):
    global m_count
    if len(a) <= 1:
        return a
    m_t1 = time.time()
    mid = len(a) // 2
    leftList = a[:mid]
    rightList = a[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)

    return merge(leftList, rightList)


def merge(left, right):
    global m_count
    result = []
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

            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:

            result.append(right[0])
            right = right[1:]
        # print(result)
    # print(result)
    m_t2 = time.time()
    return result


def make_random_array(n):
    random_array = []
    while len(random_array) < n:
        temp = (random.randint(1, n))
        if temp not in random_array:
            random_array.append(temp)
    return random_array


if __name__ == '__main__':

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
        elif num == 4:
            print("Qucik 1")
        elif num == 5:
            print("Quick 2")
        elif num == 6:
            print("Quick 3")
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
