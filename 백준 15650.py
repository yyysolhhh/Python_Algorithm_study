# 1 시간 더 적게 걸림
def series():
    if len(combi) == M:
        print(' '.join(map(str, combi)))
        return
    for i in range(1, N+1):
        if combi:
            if i in combi or i <= combi[-1]:
                continue
        combi.append(i)
        series()
        combi.pop()

# 2


def series2(start):
    if len(combi) == M:
        print(' '.join(map(str, combi)))
        return
    for i in range(start, N+1):
        if combi:
            if i in combi:
                continue
        combi.append(i)
        series2(i+1)
        combi.pop()


N, M = map(int, input().split())
combi = []
series()
series2(1)
