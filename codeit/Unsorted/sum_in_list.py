def sum_in_list(search_sum, sorted_list):
    # 코드를 쓰세요
    result = False
    a =0
    list_length = int(len(sorted_list))
    for i in range(list_length):
        for j in range(i+1,list_length):
            if sorted_list[i]+sorted_list[j]==15:
                result = True
                break
    return result
# 내가 푼방식은 brute force 방식
# 하지만 효율적인 방식은 아니다. 리스트가 정렬된 리스트라는 점을
# 이용해서 효율적으로 풀어보자.
# 여기서 효율적으로 확인하는법
# 두원소 a,b 를 둬서 a를 맨처음 원소 b를 맨마지막 원소로 둔다
# 여기서 a와 b를 더해서 결과값보다 작으면 a를 한칸씩 우측으로 이동하고
# 결과값보다 크면 b를 한칸씩 왼쪽으로 움직여서 찾는다.
'''
def sum_in_list(search_sum, sorted_list):
    # 위치 지표를 만듦
    low = 0
    high = len(sorted_list) -1

    while low< high:
        candidate_sum = sorted_list[low]+ sorted_list[high]

        if candidate_sum ==search_sum:
            return True
        if candidate_sum <search_sum:
            low+=1
        else:
            high -=1
    return False
'''
print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))