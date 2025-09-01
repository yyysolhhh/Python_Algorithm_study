D, H, M = map(int, input().split())
total = (D - 11) * 24 * 60 + (H - 11) * 60 + M - 11
if total < 0:
    print(-1)
else:
    print(total)
