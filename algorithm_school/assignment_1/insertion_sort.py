import random
import time


def insertion_sort():
    array = make_random_array(1000)
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


def heap_sort_main():
    random_array = make_random_array(1000)
    start_time = time.time()
    heap_sort(random_array)
    end_time = time.time()
    print(random_array)
    print(end_time-start_time)


def heap_sort(random_array):
    heap_size = len(random_array)
    for i in range(heap_size // 2 - 1, -1, -1):
        heapify(random_array, i, heap_size)
    for i in range(heap_size - 1, 0, -1):
        random_array[0], random_array[i] = random_array[i], random_array[0]
        heapify(random_array, 0, i)
    return random_array


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


def make_random_array(n):
    random_array = []
    while len(random_array) < n:
        temp = (random.randint(1, n))
        if temp not in random_array:
            random_array.append(temp)
    return random_array


insertion_sort()
heap_sort_main()
