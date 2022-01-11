N, M = map(int, input().split())
A = list(map(int, input().split()))
res = 0
for i in range(N):
    for j in range(i+1, N):
        if sum(A[i:j+1]) == M:
            res += 1
print(res)
