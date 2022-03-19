N = int(input())
A = list(map(int, input().split()))
sorted_A = sorted(A)
P = []
for i in A:
    idx = sorted_A.index(i)
    P.append(idx)
    sorted_A[idx] = 0
print(*P)

# 틀림
# P = [0 for _ in range(N)]
# A2 = sorted(A)
# for i in range(N):
#     for j in range(N):
#         if A[i] == A2[j]:
#             P[i] = j
# print(*P)
