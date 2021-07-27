N = int(input())


def hansu(N):
    hansu = 0
    for i in range(1, N+1):
        X = list(map(int, str(i)))
        if i < 100:
            hansu += 1
        elif X[2] - X[1] == X[1] - X[0]:
            hansu += 1
    return hansu


print(hansu(N))
