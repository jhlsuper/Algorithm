from _collections import deque


def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    answer = 0

    for i in cities:
        i = i.lower()
        if i in cache:
            cache.remove(i)
            cache.append(i)
            answer +=1
        else:
            cache.append(i)
            answer+=5
    return answer
