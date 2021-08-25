# 14~23줄
# import sys
# S = sys.stdin.readline()
# i = 0
# while i <= len(S):
#     if S[i] == "<":
#         while S[i] != ">":
#             i += 1
#         i += 1
#     elif S[i].isalnum():
#         start = i
#         while S[i] != "<":
#             i += 1
#         # word = S[start:i]
#         word = S[i-1:start-1:-1]
#         print(word)
#         # word.reverse()
#         # print(word)
#         # S[start:i] = S[i-1:start-1:-1]
#         S[start:i] = word
#         # word = "".join(reversed(S[start:i]))
#         # S[start:i].reverse()
#         # S[start:i] = list(S[i:start:-1])
#         print(S)
#     elif S[i] == " ":
#         i += 1
# print(S)
# # print(tag+string[::-1], end='')
# # print(" ", end='')

import sys
S = sys.stdin.readline()
tag = False
ans = []
mid = []
reverse = []
index = []
for i in range(len(S)):
    if S[i] == "<":
        tag = True
        ans.append(S[i])
        continue
    elif S[i] == ">":
        tag = False
        ans.append(S[i])
        index.append(i)
        continue
    if tag == True:
        ans.append(S[i])
    else:
        mid.append(S[i])
    mid = "".join(mid).strip()
    for i in mid.split():
        reverse.append(i[::-1])
        reverse.append(" ")

ans.insert(index[int((len(index)/2-1))]+1, "".join(reverse).strip())
print("".join(ans))
