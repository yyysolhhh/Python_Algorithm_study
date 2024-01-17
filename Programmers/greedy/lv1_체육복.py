def solution(n, lost, reserve):
    answer = n - len(lost)
    lost_re = []
    reserve.sort()
    lost.sort()
    for i in lost:
        if i in reserve:
            answer += 1
            reserve.remove(i)
        else:
            lost_re.append(i)
    for i in lost_re:
        if i - 1 in reserve:
            answer += 1
            reserve.remove(i - 1)
        elif i + 1 in reserve:
            answer += 1
            reserve.remove(i + 1)
    return answer


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [1, 2], [2, 3]))
print(solution(5, [2, 4], [3, 1]))
