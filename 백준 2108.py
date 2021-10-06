N = int(input())
num = []
mean, med, mod, rng = 0, 0, 0, 0
for _ in range(N):
    num.append(int(input()))
num.sort()
# mean
for i in num:
    mean += i
mean = mean//len(num)
# median
med = num[len(num)//2]
# mode
count = {}
for i in num:
    count[i] = num.count(i)
count = sorted(count.items(), key=lambda x: (x[1], x[0]))
if len(count) > 1:
    if count[0][1] == count[1][1]:
        mod = count[1][0]
    # else:
    #     mod = count[0][0]
else:
    mod = count[0][0]
# range
rng = num[-1] - num[0]
# print
print(mean)
print(med)
print(mod)
print(rng)
