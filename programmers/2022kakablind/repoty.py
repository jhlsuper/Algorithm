def solution(id_list, report, k):
    answer = []
    gotReport =[]
    dict ={}
    for i in id_list:
        ## 신고 당한 횟수, 본인을 신고한 사람 리스트, 신고한 사람 리스트
        dict[i] =[0,[],[]]
    # print(dict)
    for i in report:
        
        
        temp = i.split()
        if temp[0] not in dict[temp[1]]:
            dict[temp[1]][0]+=1
            dict[temp[1]][1].append(temp[0])
        if temp[1] not in dict[temp[0]][2]:
            dict[temp[0]][2].append(temp[1])
    
    for key,elememt in dict.items():
        if(elememt[0]>=k):
            gotReport.append(key)
    # print(gotReport)
    for i in dict.values():
        temp =0
        for j in i[2]:
            if j in gotReport:
                temp+=1
        answer.append(temp)
    # print(answer)
    return answer


solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)