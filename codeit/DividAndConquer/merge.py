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


print(merge([1, 2, 3, 4], [5, 6, 7, 8]))
print(merge([5, 6, 7, 8], [1, 2, 3, 4]))
print(merge([4, 7, 8, 9], [1, 3, 6, 10]))
