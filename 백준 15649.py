def addNum():
    if len(combi) == M:
        print(' '.join(map(str, combi)))
        return
    for i in range(1, N+1):
        if i in combi:
            continue
        combi.append(i)
        print(combi)
        addNum()
        combi.pop()


N, M = map(int, input().split())
combi = []
addNum()
