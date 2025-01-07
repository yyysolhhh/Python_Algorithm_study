N, L, R = map(int, input().split())
A = list(map(int, input().split()))
A[L - 1:R] = sorted(A[L - 1:R])
#ans = 1
#for i in range(N - 1):
#    if A[i] > A[i + 1]:
#        ans = 0
#        break
print(int(all(A[i] <= A[i + 1] for i in range(N - 1))))
