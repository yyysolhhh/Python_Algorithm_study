from itertools import combinations
N = int(input())
S = []
S_pair = []
gap = []
for _ in range(N):
    S.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if i == j:
            break
        S_pair.append(S[i][j] + S[j][i])
# print(list(combinations(S_pair, N//2)))
for i in range(N):
    for j in range(i+1, N):
        gap.append(abs(S_pair[i] - S_pair[j]))
print(min(gap))
