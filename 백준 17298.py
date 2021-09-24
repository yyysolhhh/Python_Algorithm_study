N = int(input())
A = list(map(int, input().split()))
oks = [-1 for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        if A[i] < A[j]:
            oks[i] = A[j]
            break
print(' '.join(map(str, oks)))
