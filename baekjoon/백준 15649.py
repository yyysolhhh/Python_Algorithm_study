from itertools import permutations

# 1 맞음


def addNum():
    if len(combi) == M:
        print(' '.join(map(str, combi)))
        return
    for i in range(1, N+1):
        if i in combi:
            continue
        combi.append(i)
        addNum()
        combi.pop()


N, M = map(int, input().split())
combi = []
addNum()

# 2 맞음
N, M = map(int, input().split())
perm = list(permutations(range(1, N+1), M))
for i in perm:
    print(*i)
