dist = int(input())
ans = 0
for i in range(len(str(dist))):
    d = dist % 10
    dist //= 10
    if d > 4:
        ans += (d - 1) * (9 ** i)
    else:
        ans += d * (9 ** i)
print(ans)
