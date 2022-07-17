S = input()
strs = []
for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        strs.append(S[i:j])
print(len(set(strs)))
