N = int(input())
M = int(input())
S = input()
PN = 'IO' * N + 'I'
cnt = 0
for i in range(len(S) - len(PN)):
    if S[i:i+len(PN)] == PN:
        cnt += 1
print(cnt)
