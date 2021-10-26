N, K = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))
# 1 시간초과
# sum, num = 0, 0
# for i in list(reversed(A)):
#     if i < K:
#         while sum <= K:
#             if sum + i > K:
#                 break
#             sum += i
#             num += 1
# print(num)
# 2
res = 0
for i in list(reversed(A)):
    res += K // i
    K %= i
    if K == 0:
        break
    print(i, K)
print(res)
