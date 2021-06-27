def solution(n, arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        binary = str(bin(i | j)[2:])
        binary = binary.rjust(n, '0')
        binary = binary.replace("1", '#')
        binary = binary.replace('0', ' ')
        answer.append(binary)

    return answer
solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
