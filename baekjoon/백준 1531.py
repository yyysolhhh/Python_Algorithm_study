N, M = map(int, input().split())
pic = [[0 for _ in range(100)] for _ in range(100)]
res = 0
for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(lx-1, rx):
        for j in range(ly-1, ry):
            pic[j][i] += 1
for i in range(100):
    for j in range(100):
        if pic[j][i] > M:
            res += 1
print(res)
