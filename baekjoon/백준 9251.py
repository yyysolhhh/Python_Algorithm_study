str1 = input()
str2 = input()
lcs = [[0 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
# max_len = 0
for i in range(1, len(str2) + 1):
    for j in range(1, len(str1) + 1):
        if str1[j - 1] == str2[i - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])
# for i in range(len(str2) + 1):
#     max_len = max(max_len, max(lcs[i]))
# print(max_len)
print(lcs[-1][-1])
