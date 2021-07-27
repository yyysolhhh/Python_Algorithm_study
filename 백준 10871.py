N, X = map(int, input().split())
A = list(map(int, input().split()))
if len(A) == N:
    for i in A:
        if i < X:
            print(i, end=' ')
