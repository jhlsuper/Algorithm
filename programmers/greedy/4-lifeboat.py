def solution(people, limit):
    answer = len(people)

    new_people = sorted(people, reverse=True)
    i = 0
    j = len(new_people) - 1
    print(new_people)
    while i< j:
        if new_people[i] + new_people[j] <= limit:
            j -= 1
            answer -= 1
        i += 1
    return answer


solution([70, 50, 80, 50], 100)
