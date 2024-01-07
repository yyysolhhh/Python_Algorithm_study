#s = input()
#res = 0
#for i, c in enumerate(s[1:]):
#    if c != s[i]:
#        res += 1
#if res % 2 == 0:
#    print(res // 2)
#else:
#    print(res // 2 + 1)

# 다른 풀이
s = input()
res = 1
for i, c in enumerate(s[1:]):
    if c != s[i]:
        res += 1
print(res // 2)
