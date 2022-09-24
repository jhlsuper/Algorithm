def solution(cap, n, deliveries, pickups):
    answer = -1
    emptySpace = cap
    pickupSize =0
    deliverSize =0
    delDict= dict(zip(range(1,n+1),deliveries))
    pickDict= dict(zip(range(n),pickups))
    sortedDict = (sorted(pickDict.items(),key =lambda item:item[1],reverse =True))
    print(sortedDict)
    for i in sortedDict:
        print(i[1])
    
    return answer

solution(4,5,[1,0,3,1,2],[0,3,0,4,0])