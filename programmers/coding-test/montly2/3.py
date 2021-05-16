import heapq


def solution(s):
    answer = []
    temp = []
    list = []
    for i in s:
        for j in (list(i)):
            while j == 0:
                temp.append[j]
            list.append(temp,)
    return answer


solution(["1110", "100111100", "0111111010"])


def solution(s):
    return [disassemble(ss) for ss in s]


def disassemble(s):
    # 문자열의 모든 110들 (시작 인덱스, 1 개수)
    arr = get_all_zzo(s)
    while 0 < len(arr):
        one, idx = heapq.heappop(arr)
        one = -one  # 내림차순 위해 마이너스 붙였으므로

        # 111...110 의 자리를 바꿈 111..1110~ -> 1...1 110~ -> 110 1...1~ -> 1101...1~
        s = s[:idx - one + 2] + "110" + s[idx - one + 2:idx] + s[idx + 3:]

        # 자리 바꾼 110 이후의 인덱스
        from_ = idx - one + 2 + 3

        # 해당 인덱스에서부터 다시 110을 찾고 큐에 넣음
        new_zzo = get_zzo(from_, s)
        if new_zzo is not None:
            new_one, new_idx = new_zzo
            heapq.heappush(arr, (-new_one, new_idx))

    return s


def get_all_zzo(s):
    arr = []
    i = 0
    while i < len(s):
        # i 이후의 110
        zzo = get_zzo(i, s)
        if zzo is None:
            # 해당 인덱스부터 110 시작 안 하면 다음 인덱스로
            i += 1
            continue
        j, idx = zzo

        # 110 우선순위 큐에 넣어줌
        heapq.heappush(arr, (-j, idx))

        # 110 다음 인덱스
        i = i + j + 1
    return arr


def get_zzo(from_, s):
    # from 이후의 110을 찾음
    j = 0
    while from_ + j < len(s) and s[from_ + j] != '0':
        j += 1

    # 110 찾음 (j는 1의 개수)
    if 2 < j and from_ + j < len(s):
        return j, from_ + j - 2
    return None
