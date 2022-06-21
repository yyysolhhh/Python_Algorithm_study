def solution(array, commands):
    answer = []
    for c in commands:
        i = c[0] - 1
        j = c[1] - 1
        k = c[2] - 1
        answer.append(sorted(array[i:j+1])[k])
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
