n = int(input())
dp = []
for i in range(1, n):
    if i == 1:
        dp.append(1)
    elif i == 2:
        dp.append(3)
    else:
        dp.append()
print(dp[-1] % 10007)
