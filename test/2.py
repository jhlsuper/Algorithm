## 선호 순위  희망 기업

## 1단계 거절당하지 않은 기업 중에서 자신의 선호도가 가장 높은 기업 한곳에 지원
## 입사 희망 기업으로 부터 모두 거절당하면 지원 중단

## 2단계 선호도가 높은 순서대로 지원자를 잠성 선택  선택 x -> 거절

## 거절당한 지원자들 중에서 다른 기업에 지원할 지원자가 있다면 1단계 반복

##return 기업마다 이름 + 오름차순 지원자 이름

def solution(companies, applicants):
    global arr, app, length, pop, app_name, temp_array, discard
    answer = []
    arr = []  ## 현황 배열
    app = []  ## 지원자 정보
    length = []  ## 각 기업이 뽑는 수
    pop = []  ##선호도 배열
    app_name = []
    temp_array = []
    discard = []  ##탈락한 사람들
    for i in (companies):
        arr.append([])
        temp_array.append([])
        temp = i.split()
        temp2 = []
        for j in range(len(temp[1])):
            temp2.append(temp[1][j])
        pop.append(temp2)

        length.append(int(temp[2]))
    for i in range(len(applicants)):
        temp = applicants[i].split()
        temp_arr = []
        app_name.append(temp[0])
        for j in range(int(temp[2])):
            temp_arr.append(temp[1][j])
        app.append(temp_arr)
    ## 준비 끝 지원 시작

    while len(temp) != 0:
        apply(discard)
        select()
        temp = discard

    for i in arr:
        i.sort()

    for i in range(len(companies)):
        temp = companies[i].split()[0] + "_"
        for j in arr[i]:
            temp += j

        answer.append(temp)

    return answer


def apply(discard):
    if len(discard) > 0:

        for i in discard:
            temp = ord(i) - 97

            if (app[temp]):
                temp2 = app[temp][0]
                app[temp].remove(app[temp][0])
                arr[ord(temp2) - 65].append(app_name[temp])
        discard.clear()
    else:

        for i in range(len(app)):
            temp = app[i][0]
            app[i].remove(app[i][0])

            arr[ord(temp) - 65].append(app_name[i])


def select():
    for i in range(len(arr)):
        if arr[i]:
            for j in pop[i]:

                if j in arr[i]:

                    if len(temp_array[i]) < length[i]:
                        temp_array[i].append(j)
                    else:
                        discard.append(j)
                        arr[i].remove(j)
    for i in temp_array:
        i.clear()


def calc_sum():
    sum = 0
    for i in arr:
        sum += len(i)
    return sum


solution(["A fabdec 2", "B cebdfa 2", "C ecfadb 2"], ["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"])
