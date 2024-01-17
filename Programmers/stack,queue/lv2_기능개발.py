def solution(progresses, speeds):
    answer = []

    while progresses:
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while progresses:
            if (progresses[0] >= 100):
                progresses.pop(0)
                cnt += 1
            else:
                break
        if cnt:
            answer.append(cnt)
    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]
# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))
