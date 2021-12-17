N, M = map(int, input().split())
res = 0
for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    res += (rx - lx) * (ry - ly)
print(res)
