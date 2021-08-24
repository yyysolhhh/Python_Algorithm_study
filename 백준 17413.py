import sys
S = sys.stdin.readline()
i = 0
word = []
while i <= len(S):
    if S[i] == "<":
        while S[i] != ">":
            i += 1
    elif S[i].isalnum():
        start = i
        while S[i] != "<":
            i += 1
        word = list(S[start:i].split())
        S[start:i] = word.reverse()
print(S)
# print(tag+string[::-1], end='')
# print(" ", end='')
