N = int(input())
S = input()
res = 1
for i, c in enumerate(S):
    if i > 0 and c != S[i - 1]:
        res += 1
print(res)
