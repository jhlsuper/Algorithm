## 모든 달은 28일까지 있다.  2022.05.19 



def addMonth(date, month):
    # print(date,month)
    temp = date.split(".")
    if(12- (month+int(temp[1]))>0):
        temp[1]=month +int(temp[1])
        
        
    else:
        # print("over")
        temp[0]=int(temp[0])+1
        temp[1] = int(temp[1])+month-12
    if(int(temp[2])
    temp[2] = int(temp[2])-1
    return str(temp[0])+'.'+str(temp[1])+"."+ str(temp[2])
def compare(today,addedDate):
    todaySplit= today.split('.')
    todayYear,todayMonth,todayDay = int(todaySplit[0]),int(todaySplit[1]),int(todaySplit[2])
    addedSplit =addedDate.split('.')
    addedYear,addedMonth,addedDay = int(addedSplit[0]),int(addedSplit[1]),int(addedSplit[2])
    print(today, addedDate)
    if(todayYear<addedYear):
        return True
    else:
        if(todayMonth<addedMonth):
            return True
        else:
            if(todayDay<addedDay):
                return True
    return False
def solution(today, terms, privacies):
    
    # print(todayYear,todayMonth,todayDay)
    answer = []
   
    term ={} 
    for i in terms:
        # print(i.split())
        term[i[0]]= int(i.split()[1])
    # print(term)
    for i in privacies:
        termSplit =i.split(".")
        # print(termSplit)
        date = termSplit[0]+"."+termSplit[1]+"."+termSplit[2].split()[0]
        addDate =(addMonth(date,term[termSplit[2].split()[1]]))
        # print(compare(today,addDate))
        if ( compare(today,addDate)):
            answer.append(privacies.index(i))
    print(answer)
    return answer


solution("2022.05.19",["A 6","B 12","C 3"],["2021.05.02 A", "2021.07.01 B","2022.02.19 C", "2022.02.20 C"])