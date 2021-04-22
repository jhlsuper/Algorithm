def solution(numbers, target):
    n = len(numbers)
    answer = 0

    def dfs(index, result):
        if index == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(index+1, result+numbers[index])
            dfs(index+1, result-numbers[index])
    dfs(0, target)

    return answer
