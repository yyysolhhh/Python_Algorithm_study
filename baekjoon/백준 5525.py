N = int(input())
M = int(input())
S = input()

# 2
IOI = 0
PN = 0
i = 1
while i < M-1:
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] == 'I':
        IOI += 1
        if IOI == N:
            PN += 1
            IOI -= 1
        i += 1
    else:
        IOI = 0
    i += 1
print(PN)

# 1 시간 초과
# PN = 'IO' * N + 'I'
# cnt = 0
# for i in range(M - len(PN)):
#     if S[i:i+len(PN)] == PN:
#         cnt += 1
# print(cnt)
