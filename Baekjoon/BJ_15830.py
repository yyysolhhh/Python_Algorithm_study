V, W, D = map(int, input().split())
t = W / V
s = 5 * t ** 2
cnt = 0
while s < D:
    t *= 1 / 0.8
    s += 5 * t ** 2
    cnt += 1
print(cnt)
