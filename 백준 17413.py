import sys
S = sys.stdin.readline()
i = 0
word = []
while i <= len(S):
    if S[i] == "<":
        while S[i] != ">":
            i += 1
            print(1)
        i += 1
    elif S[i].isalnum():
        start = i
        while S[i] != "<":
            i += 1
            print(2)
        # word = list(reversed(S[start:i]))
        # S[start:i] = word
        # S[start:i].reverse()
        S[start:i] = list(S[i:start:-1])
        print(S)
    elif S[i] == " ":
        i += 1
print(S)
# print(tag+string[::-1], end='')
# print(" ", end='')
