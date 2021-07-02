import datetime


def solution(lines):
    # 요청 처리를 끝낸 시간 / 요청이 들어온 시간 저장
    end_times, start_times = [], []
    for i in lines:
        tmp = i.split()
        # et = 요청이 끝난 연월일시. dur = 요청이 처리되기까지의 시간.
        et, dur = "".join(tmp[0] + "T" + tmp[1]), float(tmp[2][:-1])
        # datetime 형태로 변환
        et = datetime.datetime.fromisoformat(et)
        dur = datetime.timedelta(seconds=dur)

        # 각 배열에 저장.
        end_times.append(et)
        start_times.append(et - dur + datetime.timedelta(seconds=0.001))

    # 시작한 시간과 끝난 시간의 배열을 합친다. (처리량이 변화할 때는 새 요청이 들어올 때 / 요청이 끝날 때뿐이므로)
    total = start_times + end_times

    # 윈도우 기준 = 1초.
    sec = datetime.timedelta(seconds=1)
    max_ = 0
    for starts in total:
        result = 0
        for j in range(len(end_times)):
            # 해당 로그 기준으로 1초 안에 다른 요청이 처리 완료되었거나, 다른 요청이 새로 들어온 경우
            if starts <= end_times[j] < starts + sec or starts <= start_times[j] < starts + sec:
                result += 1
            # 아니면, 해당 로그 이전에 요청이 들어와서 1초 안에 요청이 끝나지 않은 경우. 1초 윈도우 전체가 포함된 경우를 말함.
            elif start_times[j] <= starts and end_times[j] >= starts + sec:
                result += 1
        if max_ < result:
            max_ = result
    return max_

############아 모르겠다##################