N = int(input())
M = int(input())
S = input()

# 2
cnt = 0
I = 0
PN = 0
while i <= N:
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] == 'I':
        i += 1
        if i == N:
            PN += 1
    else:
        i = 0


# 1 시간 초과
# PN = 'IO' * N + 'I'
# cnt = 0
# for i in range(M - len(PN)):
#     if S[i:i+len(PN)] == PN:
#         cnt += 1
# print(cnt)
