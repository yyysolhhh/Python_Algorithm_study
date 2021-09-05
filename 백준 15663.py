def series():
    if len(combi) == M:
        print(' '.join(map(str, combi)))
        return
    for i in num:
        if i not in combi:
            combi.append(i)
            series()
            combi.pop()


N, M = map(int, input().split())
num = set(map(int, input().split()))
num = sorted(list(num))
print(num)
combi = []
series()
