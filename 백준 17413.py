import re
S = input()
S = re.split("<|>", S)
print(S)
for word in S:
    print(word[::-1], end='')
    print(" ", end='')
