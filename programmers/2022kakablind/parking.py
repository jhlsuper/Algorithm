def solution(fees, records):
    ## 차량번호가 작은 자동차 부터
    ## fees 기본시간 기본요금, 단위시간, 단위요금
    dict ={}
    answer = []
    for i in records:
 
        temp = i.split()
        if(temp[2]=='IN'):
            dict[temp[1]]=temp[0]
        else:
           start = dict[temp[1]]
           end = i.split()[0]
           start_time =(start.split(':'))
           end_time = end.split(':')
        #    print(start_time, end_time)
           minDiff = (int(end_time[0])*60 + int(end_time[1])) - (int(start_time[0])*60+ int(start_time[1]))
           
           if(minDiff <=fees[0]):
            answer.append(fees[1])
            
    
       
    return answer




solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])