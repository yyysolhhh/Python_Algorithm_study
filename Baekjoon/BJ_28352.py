# 1
N = int(input())
fac = 1
for i in range(2, N + 1):
    fac *= i
ans = fac // 60 // 60 // 24 // 7
print(ans)

# 2
N = int(input())
ans = 6
for i in range(11, N + 1):
    ans *= i
print(ans)
