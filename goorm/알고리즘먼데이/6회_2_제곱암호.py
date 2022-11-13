# 틀림
N = int(input())
S = input()
res = ''
for i, ch in enumerate(S):
    if i % 2 == 0:
        temp = ord(ch) + int(S[i + 1]) ** 2
        if temp > 122:
            temp -= 26
        res += chr(temp)
print(res)
