A, B = map(int, input().split())
series = []
res = 0
for i in range(1, 46):
    for _ in range(i):
        series.append(i)
for i in series[A-1:B]:
    res += i
print(res)
