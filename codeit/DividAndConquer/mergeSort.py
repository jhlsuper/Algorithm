def merge(list1, list2):
    merged_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            j += 1
    if i == len(list1):
        for s in range(j, len(list2)):
            merged_list.append(list2[s])
    if j == len(list2):
        for u in range(i, len(list1)):
            merged_list.append(list1[u])

    return merged_list


def merge_sort(list):
    if len(list) < 2:
        return list
    left = list[:len(list)//2]
    right = list[len(list)//2:]
    return merge(merge_sort(left), merge_sort(right))


print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
