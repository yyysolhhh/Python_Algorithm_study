#s = input()
#res = 0
#for i, c in enumerate(s[1:]):
#    if c != s[i]:
#        res += 1
#if res % 2 == 0:
#    print(res // 2)
#else:
#    print(res // 2 + 1)

# 2
#s = input()
#res = 1
#for i, c in enumerate(s[1:]):
#    if c != s[i]:
#        res += 1
#print(res // 2)

# 3
s = input()
print(max(s.count("01"), s.count("10")))
