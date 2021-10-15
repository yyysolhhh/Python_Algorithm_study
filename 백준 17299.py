import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
F = []
NGF = []
for i in A:
    F.append(A.count(i))
for i in range(N):
    for j in range(i+1, N):
        # print(F[i], F[j])
        if F[i] < F[j]:
            # print('!')
            NGF.append(A[j])
            break
    else:
        NGF.append(-1)
        # print('?')
print(*NGF)
