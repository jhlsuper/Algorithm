def solution(people, limit):
    answer = 0
    new_limit = limit
    count = 0
    people.sort()
    while len(people) > 0:

        while new_limit > 0:
            if count == 2:
                break
            if len(people) == 1:
                people.remove(people[0])

                answer += 1
                break
            new_limit -= min(people)
            if new_limit >= 0:
                people.pop()
                count += 1
        print(count)
        print(people)
        answer += 1
        count = 0
        new_limit = limit

    return answer


solution([70, 50, 80, 50], 100)
