import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
# 시간 초과
# F = []
# NGF = []
# for i in A:
#     F.append(A.count(i))
# for i in range(N):
#     for j in range(i+1, N):
#         # print(F[i], F[j])
#         if F[i] < F[j]:
#             # print('!')
#             NGF.append(A[j])
#             break
#     else:
#         NGF.append(-1)
#         # print('?')
# print(*NGF)

# 2
stack = []
F = Counter(A)
NGF = [-1 for _ in range(N)]
for i in range(N):
    while stack and F[A[stack[-1]]] < F[A[i]]:
        NGF[stack.pop()] = A[i]
    stack.append(i)
print(*NGF)
