S = input()
strs = []
for i in range(len(S) - 1):
    for j in range(i + 1, len(S) + 1):
        strs.append(S[i:j])
print(strs)
print(set(strs))
print(len(set(strs)))
