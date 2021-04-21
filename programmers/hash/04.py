import operator
from collections import defaultdict


# def solution(genres, plays):

#     answer = []
#     dict = {}
#     value_list = []
#     temp = []

#     for i in range(len(genres)):
#         # print(i) 0,1,2,3,4
#         if genres[i] not in dict:
#             dict[genres[i]] = [plays[i]]

#         elif len(dict[genres[i]]) == 1:
#             dict[genres[i]].append(plays[i])
#         elif len(dict[genres[i]]) == 2:
#             if min(dict[genres[i]]) >= plays[i]:
#                 pass
#             else:
#                 dict[genres[i]].append(plays[i])
#                 dict[genres[i]].remove(min(dict[genres[i]]))

#     for j in dict.values():
#         value_list.append(sorted(j, reverse=True))

#     c = sorted(value_list, key=lambda x: -max(x[0], x[1]))
#     # print(c)
#     for i in (c):
#         for j in range(len(i)):
#             temp.append(i[j])
#     # print(temp)
#     for i in temp:
#         answer.append(plays.index(i))
#     # print(answer)
#     return answer
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum(map(lambda y: y[0], d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer

solution(["classic", "pop", "classic", "classic", "pop"],
         [500, 600, 150, 800, 2500])
