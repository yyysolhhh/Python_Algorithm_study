N = int(input())
if N == 0:
    print(0)
else:
    cur = 1
    ans = 1
    while cur < N:
        cur *= 2
        ans += 1
    print(ans)
