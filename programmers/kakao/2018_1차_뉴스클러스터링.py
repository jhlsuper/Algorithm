def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1_list = makelist(str1)
    str2_list = makelist(str2)

    # print(str1_list)
    # print(str2_list)
    answer = cal(str1_list, str2_list)
    print(answer)
    return answer


def makelist(str):
    str_list = []
    for i in range(len(str)):
        # print(str1[i:i + 2])
        if str[i:i + 2].isalpha() and len(str[i:i + 2]) == 2:
            str_list.append(str[i:i + 2])
    return str_list


def cal(list1, list2):
    jaccard = 0

    inter_list, union_list = inter_union(list1,list2)
    # print(len(union_list), union_list)
    # print(len(inter_list), inter_list)
    if len(inter_list) == 0:
        jaccard = 1
        return jaccard*65536
    # if union_list == intersection_list:
    #     jaccard = max(len(list1), len(list2)) / (len(list1) + len(list2))
    #     print(jaccard)
    #     return int(jaccard * 65536)
    else:
        jaccard = len(inter_list) / len(union_list)
        return int(jaccard * 65536)


def union(list1, list2):
    u_list1 = list1
    u_list2 = list2
    union_list = []
    for i in u_list1:
        union_list.append(i)
        u_list2.remove(i)
    for i in u_list2:
        union_list.append(i)
    return union_list


def inter_union(list1, list2):
    if len(list1)>len(list2):
        intersect_list = [list1.remove(i) for i in list2 if i in list1]
    else:
        intersect_list=[list2.remove(i) for i in list1 if i in list2]

    union_list = list1+list2
    return intersect_list,union_list


solution("aa1+aa2", "AAAA12")
