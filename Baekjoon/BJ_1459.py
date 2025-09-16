# 1
X, Y, W, S = map(int, input().split())
if 2 * W < S:
    print((X + Y) * W)
else:
    ans = S * min(X, Y)
    if W > S:
        if (X + Y) & 1 == 0:
            ans += abs(X - Y) * S
        else:
            ans += abs(X - Y - 1) * S + W
    else:
        ans += abs(X - Y) * W
    print(ans)

# 2
X, Y, W, S = map(int, input().split())
if (X + Y) & 1 == 0:
    case1 = max(X, Y) * S
else:
    case1 = (max(X, Y) - 1) * S + W
case2 = (X + Y) * W
case3 = min(X, Y) * S + abs(X - Y) * W
print(min(case1, case2, case3))
