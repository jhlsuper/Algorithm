def solution(id_list, report, k):
    dict = {}
    name_dict = {}
    answer_dict = {}
    bigger = []
    new_report = set(report)

    for i in id_list:
        dict[i] = 0
        answer_dict[i] = 0
        name_dict[i] = []
    for j in new_report:
        dict[j.split()[1]] += 1
        name_dict[j.split()[0]].append(j.split()[1])

    # print(dict)
    # print(name_dict)
    for key, value in dict.items():
        if value >= k:
            bigger.append(key)
    # print(bigger)
    for key,value in name_dict.items():

        for j in value:
            if j in bigger:
                answer_dict[key]+=1

    return list(answer_dict.values())


solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2)
