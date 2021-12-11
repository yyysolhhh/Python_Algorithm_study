N = int(input())
A = list(map(int, input().split()))


# P = {}
# for i in range(N):
#     P[A[i]] = i
# print(P)
# P = sorted(P.items())
# print(P)

# 틀림
# P = [0 for _ in range(N)]
# A2 = sorted(A)
# for i in range(N):
#     for j in range(N):
#         if A[i] == A2[j]:
#             P[i] = j
# print(*P)
