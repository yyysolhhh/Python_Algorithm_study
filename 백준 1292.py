A, B = map(int, input().split())
series = []
res = 0
for i in range(1, 46):
    temp = i
    while temp:
        series.append(i)
        temp -= 1
for i in series[A-1:B]:
    res += i
print(res)
