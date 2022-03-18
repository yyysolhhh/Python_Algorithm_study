# S = input()
# letters = list(range(97, 123))
# for i in range(len(S)):
#     for j in letters:
#         if chr(j) == chr(j):
#             print(i)

# 1
# import string
# S = input()
# for i in string.ascii_lowercase:
#     print(S.find(i), end=' ')

# 2
# import string
# alphabet = string.ascii_lowercase
# S = input()
# for i in range(0, len(alphabet)):
#     if alphabet[i] in S:
#         print(S.index(alphabet[i]), end=' ')
#     else:
#         print(-1, end=' ')

# 3
# import string
# alphabet = string.ascii_lowercase
# S = input()
# a = []
# for i in range(0, len(alphabet)):
#     if alphabet[i] in S:
#         for j in range(0, len(S)):
#             if alphabet[i] == S[j]:
#                 if alphabet[i] in a:
#                     pass
#                 else:
#                     a.append(alphabet[i])
#                     print(j, end=' ')
#     else:
#         print(-1, end=' ')

# 4
S = input()
alphabet = list(range(97, 123))
for i in alphabet:
    print(S.find(chr(i)), end=' ')
