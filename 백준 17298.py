N = int(input())
A = list(map(int, input().split()))
oks = [-1 for _ in range(N)]
stack = [0]

# 시간 초과
# for i in range(N):
#     for j in range(i+1, N):
#         if A[i] < A[j]:
#             oks[i] = A[j]
#             break

# 스택 이용
for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        oks[stack.pop()] = A[i]
    stack.append(i)

print(*oks)
