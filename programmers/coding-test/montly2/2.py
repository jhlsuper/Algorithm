def solution(numbers):
    answer = []
    for n in numbers:
        i = 0
        original = n
        while n % 2 != 0:
            i += 1
            n //= 2
        answer.append(original + pow(2, i-1 if i != 0 else 0))
    return answer
