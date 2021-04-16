import operator

def solution(genres, plays):
    
    answer = []
    dict = {}

    for i in range(len(genres)):
        #print(i) 0,1,2,3,4
        if genres[i] not in dict:
            dict[genres[i]]= [plays[i]]
            
        elif len(dict[genres[i]])==1:
            dict[genres[i]].append(plays[i])
        elif len(dict[genres[i]])==2:
            if min(dict[genres[i]]) >=plays[i]:
                pass
            else:
                dict[genres[i]].append(plays[i])
                dict[genres[i]].remove(min(dict[genres[i]]))
    print(dict)
    # for i in dict:
        # print(max(dict[i]))
    # sorted_dict = sorted(dict.items(),key = operator.itemgetter(1))

    print(dict)
    return answer

##딕셔너리에 2차원배열을 넣어서 2개 까지 넣는다.
##장르별 베스트 앨범 출력 
##속한 노래가 많이 재생된 장르 
##장르내에서 가장많이 
## 고유번호 낮은게 우선
##2개의 출력값 

solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500])