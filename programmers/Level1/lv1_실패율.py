def solution(N, stages):
    stop = [0 for _ in range(N + 2)]
    players = 0
    failure_rate = {n: 0 for n in range(N + 1)}
    for i in stages:
        stop[i] += 1
        players += 1
    for st, n in enumerate(stop):
        if players == 0:
            failure_rate[st] = 0
        else:
            failure_rate[st] = n / players
            players -= n
    answer = sorted(list(failure_rate.items())[1:-1],
                    key=lambda x: x[1], reverse=True)
    return list(map(lambda x: x[0], answer))


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
