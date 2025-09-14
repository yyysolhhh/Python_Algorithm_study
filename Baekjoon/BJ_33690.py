#1 시간초과
#def palindrome(n):
#    str_n = str(n).strip()
#    return str_n == "".join(reversed(str_n))
#
#N = int(input())
#ans = 0
#for i in range(N + 1):
#    ans += palindrome(i)
#print(ans)

#2
N = int(input())
ans = 1
for i in range(1, 10):
    porindrome = i
    while porindrome <= N:
        porindrome = porindrome * 10 + i
        ans += 1
print(ans)
