N, M = map(int, input().split())
A = list(map(int, input().split()))
res = 0

# 1 시간 초과
# for i in range(N):
#     for j in range(i+1, N):
#         if sum(A[i:j+1]) == M:
#             res += 1
# print(res)

# 2
start = 0
end = 1
while end <= N:
    total = sum(A[start:end])
    if total == M:
        res += 1
        end += 1
    elif total < M:
        end += 1
    else:
        start += 1
print(res)
