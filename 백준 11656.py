# 내 풀이
S = input()
suffix = []
for i in range(len(S)):
    suffix.append(S[i:])
for i in sorted(suffix):
    print(i)

# 다른 사람 풀이
S = str(input())
S_list = []

for _ in S:
    S_list.append(S)
    S = S[1:]

for i in sorted(S_list):
    print(i)
