def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    leftList = a[:mid]
    rightList = a[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    # print(merge(leftList, rightList))
    return merge(leftList, rightList)


def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
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
        print(result)
    # print(result)
    return result


merge_sort([38, 27, 43, 3, 9, 82, 10])
